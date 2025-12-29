# src/api.py
from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from pydantic import BaseModel, Field
from pathlib import Path
import logging

from .translator import HindiTranslator

# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Initialize FastAPI
app = FastAPI(
    title="EN→HI Public Notice Translator",
    description="Domain-specific English to Hindi translation for Indian public notices",
    version="1.0.0"
)

# Initialize translator (loads model once at startup)
translator = HindiTranslator()
logger.info("✅ Translator initialized")

# Mount static files
static_path = Path(__file__).parent.parent / "static"
app.mount("/static", StaticFiles(directory=str(static_path)), name="static")


# Request/Response models
class TranslationRequest(BaseModel):
    text: str = Field(..., min_length=1, max_length=1000, description="English text to translate")
    num_beams: int = Field(4, ge=1, le=10, description="Beam search width (1-10)")
    preserve_numbers: bool = Field(True, description="Apply F3 number preservation")
    
    class Config:
        json_schema_extra = {
            "example": {
                "text": "Parking is not allowed in this area.",
                "num_beams": 4,
                "preserve_numbers": True
            }
        }


class TranslationResponse(BaseModel):
    success: bool
    translation: str
    confidence: float
    metadata: dict
    
    class Config:
        json_schema_extra = {
            "example": {
                "success": True,
                "translation": "इस क्षेत्र में पार्किंग की अनुमति नहीं है।",
                "confidence": 0.92,
                "metadata": {
                    "input_length": 7,
                    "output_length": 9,
                    "num_beams": 4,
                    "device": "cuda"
                }
            }
        }


# Routes
@app.get("/", response_class=HTMLResponse)
async def root():
    """Serve the main HTML page"""
    index_path = static_path / "index.html"
    with open(index_path, "r", encoding="utf-8") as f:
        return f.read()


@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {
        "status": "healthy",
        "model": "Helsinki-NLP/opus-mt-en-hi (fine-tuned)",
        "device": str(translator.model_wrapper.device)
    }


@app.post("/translate", response_model=TranslationResponse)
async def translate(request: TranslationRequest):
    """
    Translate English text to Hindi
    
    - **text**: English text (1-1000 characters)
    - **num_beams**: Beam search width (default: 4)
    - **preserve_numbers**: Enable F3 post-processing (default: true)
    """
    try:
        logger.info(f"Translation request: {request.text[:50]}...")
        
        result = translator.translate(
            text=request.text,
            num_beams=request.num_beams,
            preserve_numbers=request.preserve_numbers
        )
        
        if "error" in result.get("metadata", {}):
            raise HTTPException(
                status_code=500,
                detail=f"Translation error: {result['metadata']['error']}"
            )
        
        logger.info(f"Translation success: {result['translation'][:50]}...")
        
        return TranslationResponse(
            success=True,
            translation=result["translation"],
            confidence=result["confidence"],
            metadata=result["metadata"]
        )
    
    except Exception as e:
        logger.error(f"Translation failed: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/examples")
async def get_examples():
    """Get example translations for testing"""
    examples = [
        {
            "english": "Parking is not allowed.",
            "hindi": "पार्किंग की अनुमति नहीं है।"
        },
        {
            "english": "Unauthorized entry is prohibited.",
            "hindi": "अनधिकृत प्रवेश प्रतिबंधित है।"
        },
        {
            "english": "This notice is issued under Section 144 of the Criminal Procedure Code",
            "hindi": "यह नोटिस दंड प्रक्रिया संहिता की धारा 144 के अंतर्गत जारी किया गया है"
        },
        {
            "english": "Smoking is strictly forbidden in public places.",
            "hindi": "सार्वजनिक स्थानों पर धूम्रपान सख्ती से वर्जित है।"
        }
    ]
    return {"examples": examples}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
