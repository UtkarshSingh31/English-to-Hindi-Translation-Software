// static/js/app.js

const API_BASE = '';

// DOM Elements
const englishInput = document.getElementById('englishInput');
const hindiOutput = document.getElementById('hindiOutput');
const translateBtn = document.getElementById('translateBtn');
const clearBtn = document.getElementById('clearBtn');
const copyBtn = document.getElementById('copyBtn');
const examplesBtn = document.getElementById('examplesBtn');
const charCount = document.getElementById('charCount');
const btnText = document.getElementById('btnText');
const spinner = document.getElementById('spinner');
const metadata = document.getElementById('metadata');
const examplesModal = document.getElementById('examplesModal');
const closeModal = document.getElementById('closeModal');
const examplesList = document.getElementById('examplesList');

let currentTranslation = '';

// Event Listeners
englishInput.addEventListener('input', updateCharCount);
translateBtn.addEventListener('click', handleTranslate);
clearBtn.addEventListener('click', handleClear);
copyBtn.addEventListener('click', handleCopy);
examplesBtn.addEventListener('click', showExamples);
closeModal.addEventListener('click', hideExamples);
examplesModal.addEventListener('click', (e) => {
    if (e.target === examplesModal) hideExamples();
});

// Character counter
function updateCharCount() {
    const length = englishInput.value.length;
    charCount.textContent = `${length}/1000`;
    
    if (length > 900) {
        charCount.style.color = '#ef4444';
    } else {
        charCount.style.color = '#64748b';
    }
}

// Translation
async function handleTranslate() {
    const text = englishInput.value.trim();
    
    if (!text) {
        alert('Please enter some text to translate');
        return;
    }
    
    translateBtn.disabled = true;
    btnText.textContent = 'Translating...';
    spinner.classList.remove('hidden');
    hindiOutput.textContent = 'Processing...';
    hindiOutput.classList.remove('has-translation');
    metadata.classList.add('hidden');
    
    try {
        const response = await fetch(`${API_BASE}/translate`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({
                text: text,
                num_beams: parseInt(document.getElementById('numBeams').value),
                preserve_numbers: document.getElementById('preserveNumbers').checked
            })
        });
        
        if (!response.ok) {
            const error = await response.json();
            throw new Error(error.detail || 'Translation failed');
        }
        
        const data = await response.json();
        
        currentTranslation = data.translation;
        hindiOutput.textContent = data.translation;
        hindiOutput.classList.add('has-translation');
        
        displayMetadata(data);
        
    } catch (error) {
        console.error('Error:', error);
        hindiOutput.textContent = `Error: ${error.message}`;
    } finally {
        translateBtn.disabled = false;
        btnText.textContent = 'Translate';
        spinner.classList.add('hidden');
    }
}

// Display metadata
function displayMetadata(data) {
    metadata.classList.remove('hidden');
    
    const confidence = Math.round(data.confidence * 100);
    document.getElementById('confidenceBar').style.width = `${confidence}%`;
    document.getElementById('confidenceText').textContent = `${confidence}%`;
    
    document.getElementById('inputWords').textContent = `${data.metadata.input_length} words`;
    document.getElementById('outputWords').textContent = `${data.metadata.output_length} words`;
    document.getElementById('device').textContent = data.metadata.device;
}

// Clear
function handleClear() {
    englishInput.value = '';
    hindiOutput.textContent = 'Translation will appear here...';
    hindiOutput.classList.remove('has-translation');
    metadata.classList.add('hidden');
    currentTranslation = '';
    updateCharCount();
}

// Copy
async function handleCopy() {
    if (!currentTranslation) {
        alert('No translation to copy');
        return;
    }
    
    try {
        await navigator.clipboard.writeText(currentTranslation);
        
        copyBtn.innerHTML = `
            <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                <polyline points="20 6 9 17 4 12"></polyline>
            </svg>
        `;
        copyBtn.style.color = '#10b981';
        
        setTimeout(() => {
            copyBtn.innerHTML = `
                <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                    <rect x="9" y="9" width="13" height="13" rx="2" ry="2"></rect>
                    <path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"></path>
                </svg>
            `;
            copyBtn.style.color = '';
        }, 2000);
    } catch (error) {
        alert('Failed to copy');
    }
}

// Examples
async function showExamples() {
    examplesModal.classList.remove('hidden');
    
    try {
        const response = await fetch(`${API_BASE}/examples`);
        const data = await response.json();
        
        examplesList.innerHTML = '';
        
        data.examples.forEach(example => {
            const div = document.createElement('div');
            div.className = 'example-item';
            div.innerHTML = `
                <div class="example-en">${example.english}</div>
                <div class="example-hi">${example.hindi}</div>
            `;
            
            div.addEventListener('click', () => {
                englishInput.value = example.english;
                updateCharCount();
                hideExamples();
                handleTranslate();
            });
            
            examplesList.appendChild(div);
        });
        
    } catch (error) {
        examplesList.innerHTML = '<p>Failed to load examples</p>';
    }
}

function hideExamples() {
    examplesModal.classList.add('hidden');
}

// Initialize
updateCharCount();
