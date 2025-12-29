# src/model.py
import torch
from transformers import MarianMTModel, MarianTokenizer
from pathlib import Path

class TranslationModel:
    """Singleton model loader"""
    
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._initialized = False
        return cls._instance
    
    def __init__(self):
        if not self._initialized:
            self._model = None
            self._tokenizer = None
            self._device = None
            self.load_model()
            self._initialized = True
    
    def load_model(self):
        """Load model and tokenizer once"""
        # Path to your saved model
        model_path = Path(__file__).parent.parent / "model" / "best_helsinki_model"
        
        if not model_path.exists():
            raise FileNotFoundError(f"Model not found at {model_path}")
        
        print(f"📦 Loading model from {model_path}...")
        
        # Setup device
        self._device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        
        # Load tokenizer
        self._tokenizer = MarianTokenizer.from_pretrained(str(model_path))
        
        # Load model
        self._model = MarianMTModel.from_pretrained(str(model_path))
        self._model = self._model.to(self._device)
        self._model.eval()
        
        print(f"✅ Model loaded on {self._device}")
    
    @property
    def model(self):
        """Get the loaded model"""
        return self._model
    
    @property
    def tokenizer(self):
        """Get the loaded tokenizer"""
        return self._tokenizer
    
    @property
    def device(self):
        """Get the device (cuda/cpu)"""
        return self._device
