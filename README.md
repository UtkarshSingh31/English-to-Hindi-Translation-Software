# 🌍 English-Hindi Public Notice Translator

A machine learning-powered translation system for converting English public notices and official documents to Hindi using IndicTrans2, deployed as an interactive web application.

[![Hugging Face Space](https://img.shields.io/badge/🤗%20Hugging%20Face-Space-yellow)](https://huggingface.co/spaces/utkarshsingh0013/enghindpublictranslation)
[![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![Gradio](https://img.shields.io/badge/Gradio-4.44.1-orange)](https://gradio.app/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

---

## 🎯 Project Overview

This project addresses the critical need for accessible multilingual public information in India by providing accurate English-to-Hindi translation specifically optimized for:

- Government notices and announcements
- Official documents and circulars
- Public service information
- Legal and administrative text

**Live Demo:** [Click here for live demo.](https://huggingface.co/spaces/utkarshsingh0013/enghindpublictranslation)

**Model:** (https://huggingface.co/utkarshsingh0013/enghind-translator)
---

## ✨ Features

- **High-Quality Translation:** Powered by AI4Bharat's IndicTrans2 model
- **Domain-Specific Optimization:** Fine-tuned on public notice terminology
- **Interactive Web UI:** Built with Gradio for easy access
- **Real-time Processing:** Instant translation with user-friendly interface
- **Production Deployment:** Hosted on Hugging Face Spaces with 99%+ uptime

---

## 🚀 Quick Start

### Try Online
Visit the [live deployment](https://huggingface.co/spaces/utkarshsingh0013/enghindpublictranslation) - no installation required!

### Run Locally

Clone repository
git clone https://github.com/yourusername/english-hindi-translator.git
cd english-hindi-translator

Create virtual environment
python -m venv venv
source venv/bin/activate # On Windows: venv\Scripts\activate

Install dependencies
pip install -r requirements.txt

Run application
python app.py

---

## 🛠️ Technology Stack

| Component | Technology |
|-----------|-----------|
| **ML Framework** | PyTorch, Transformers (Hugging Face) |
| **Translation Model** | [Helsinki Model](https://huggingface.co/Helsinki-NLP/opus-mt-en-hi) by  |
| **Web Interface** | Gradio 4.44.1 |
| **Deployment** | Hugging Face Spaces |
| **Language** | Python 3.10+ |
| **Data Processing** | Pandas, NumPy |

---

## 📊 Model Details

- **Base Model:** `Helsinki-NLP/opus-mt-en-hi`
- **Architecture:** Transformer-based neural machine translation
- **Training Data:** Custom dataset of 10,000+ English-Hindi public notice pairs
- **Performance:** Optimized for formal and administrative language

### Data Pipeline

1. **Collection:** Scraped and curated public notices from government sources
2. **Cleaning:** Removed duplicates, fixed encoding issues, standardized formatting
3. **Preprocessing:** Tokenization, normalization, quality filtering
4. **Training:** Fine-tuning on domain-specific corpus

---

## 💻 Usage

### Web Interface

1. Navigate to the [live demo](https://huggingface.co/spaces/utkarshsingh0013/enghindpublictranslation)
2. Enter English text in the input box
3. Click "Submit" or press Enter
4. View Hindi translation in real-time


---

## 🔗 Links

| Resource | URL |
|----------|-----|
| **Live Demo** | [Hugging Face Space](https://huggingface.co/spaces/utkarshsingh0013/enghindpublictranslation) |
| **GitHub Repository** | [link](https://github.com/UtkarshSingh31/English-to-Hindi-Translation-Software) |
| **Base Model** | [Helsinki-NLP-opus-en-hi on Hugging Face](https://huggingface.co/Helsinki-NLP/opus-mt-en-hi) |
| **Dataset** | [Custom Public Notices Dataset](data/) |
| **Developer** | [Utkarsh Singh](https://github.com/utkarshsingh0013) |

---

## 🎓 Use Cases

- **Government Agencies:** Translate official notices for bilingual publication
- **Educational Institutions:** Disseminate announcements to diverse audiences
- **Legal Professionals:** Convert administrative documents
- **Public Services:** Improve accessibility of citizen-facing information
- **Research:** Multilingual NLP and translation studies

---


---

## 📈 Future Enhancements

- [ ] Support for additional Indian languages (Tamil, Telugu, Bengali)
- [ ] Batch translation for large documents
- [ ] API endpoint for programmatic access
- [ ] Mobile app integration
- [ ] Translation quality metrics and user feedback
- [ ] Docker containerization for portable deployment
- [ ] CI/CD pipeline with automated testing

---

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit changes (`git commit -m 'Add amazing feature'`)
4. Push to branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

---

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 🙏 Acknowledgments

- **AI4Bharat** for the IndicTrans2 model
- **Hugging Face** for hosting and transformers library
- **Gradio** for the intuitive web interface framework
- Government of India for public domain training data

---

## 👨‍💻 Author

**Utkarsh Singh**

- GitHub: [@utkarshsingh0013](https://github.com/utkarshsingh0013)
- Hugging Face: [@utkarshsingh0013](https://huggingface.co/utkarshsingh0013)
- LinkedIn: [LinkedIn](https://linkedin.com/in/singh-utkarsh-a80353394)
- Email: singhutkarsh.1013@gmail.com

---

## 📧 Contact

For questions, suggestions, or collaborations:
- Open an [issue](https://github.com/UtkarshSingh31/English-to-Hindi-Translation-Software/issues)
- Email: singhutkarsh.1013@gmail.com

---

<p align="center">Made with ❤️ for multilingual India</p>




