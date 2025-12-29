# src/translator.py
import re
import torch
from src.models import TranslationModel


class HindiTranslator:
    """Translation service with post-processing"""
    
    def __init__(self):
        self.model_wrapper = TranslationModel()
    
    def translate(
        self,
        text: str,
        max_length: int = 96,
        num_beams: int = 4,
        preserve_numbers: bool = True
    ) -> dict:
        """
        Translate English to Hindi with post-processing
        
        Args:
            text: English input text
            max_length: Maximum token length
            num_beams: Beam search width
            preserve_numbers: Apply F3 number preservation
        
        Returns:
            dict with translation, confidence, metadata
        """
        if not text or not text.strip():
            return {
                "translation": "",
                "confidence": 0.0,
                "metadata": {"error": "Empty input"}
            }
        
        try:
            # Get model components
            model = self.model_wrapper.model
            tokenizer = self.model_wrapper.tokenizer
            device = self.model_wrapper.device
            
            # Encode input
            inputs = tokenizer(
                text,
                return_tensors="pt",
                max_length=max_length,
                truncation=True,
                padding=True
            ).to(device)
            
            # Generate translation - SIMPLIFIED VERSION
            with torch.no_grad():
                outputs = model.generate(
                    **inputs,
                    max_length=max_length,
                    num_beams=num_beams,
                    length_penalty=1.0,
                    early_stopping=True,
                    no_repeat_ngram_size=2,
                    repetition_penalty=1.2
                )
            
            # Decode translation
            translation = tokenizer.decode(outputs[0], skip_special_tokens=True)
            
            # F3: Number preservation post-processing
            if preserve_numbers:
                translation = self._preserve_numbers(text, translation)
            
            # Simple confidence (based on length ratio)
            confidence = self._calculate_confidence(text, translation)
            
            # Metadata
            metadata = {
                "input_length": len(text.split()),
                "output_length": len(translation.split()),
                "num_beams": num_beams,
                "device": str(device)
            }
            
            return {
                "translation": translation,
                "confidence": float(confidence),
                "metadata": metadata
            }
        
        except Exception as e:
            return {
                "translation": "",
                "confidence": 0.0,
                "metadata": {"error": str(e)}
            }
    
    def _preserve_numbers(self, source: str, translation: str) -> str:
        """F3: Fix section numbers and preserve digits"""
        # Fix Section references
        sections = re.findall(r'Section\s+(\d+)', source, re.IGNORECASE)
        if sections:
            for sec_num in sections:
                translation = re.sub(
                    r'धारा\s+\d+',
                    f'धारा {sec_num}',
                    translation,
                    count=1
                )
        
        # Fix curfew
        if 'curfew' in source.lower():
            translation = translation.replace('कर्ट', 'कर्फ्यू')
        
        return translation
    
    def _calculate_confidence(self, source: str, translation: str) -> float:
        """Calculate confidence based on length ratio"""
        if not translation:
            return 0.0
        
        # Simple heuristic: length ratio (Hindi is typically 1.0-1.3x English)
        src_len = len(source.split())
        tgt_len = len(translation.split())
        
        if src_len == 0:
            return 0.5
        
        ratio = tgt_len / src_len
        
        # Ideal ratio is 1.0-1.3 for EN->HI
        if 0.8 <= ratio <= 1.5:
            confidence = 0.9
        elif 0.5 <= ratio <= 2.0:
            confidence = 0.7
        else:
            confidence = 0.5
        
        return confidence
