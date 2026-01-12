// CosmosAI Main JavaScript - AI-Powered Version
// Uses Gemini API for autonomous, intelligent responses

// Rate Limiting
let lastCallTime = 0;
const COOLDOWN_MS = 3000; // 3 second cooldown between API calls

function checkCooldown() {
    const now = Date.now();
    if (now - lastCallTime < COOLDOWN_MS) {
        const remaining = Math.ceil((COOLDOWN_MS - (now - lastCallTime)) / 1000);
        showToast(`Please wait ${remaining} second(s)...`, 'warning');
        return false;
    }
    lastCallTime = now;
    return true;
}

// Toast Notification System
function showToast(message, type = 'info') {
    let toast = document.getElementById('cosmos-toast');
    if (!toast) {
        toast = document.createElement('div');
        toast.id = 'cosmos-toast';
        toast.style.cssText = `
            position: fixed;
            bottom: 20px;
            right: 20px;
            padding: 15px 25px;
            border-radius: 10px;
            color: white;
            font-weight: 500;
            z-index: 9999;
            opacity: 0;
            transition: opacity 0.3s ease;
            max-width: 350px;
            box-shadow: 0 4px 20px rgba(0,0,0,0.3);
        `;
        document.body.appendChild(toast);
    }

    const colors = {
        info: 'linear-gradient(135deg, #00d2ff, #007bff)',
        warning: 'linear-gradient(135deg, #ffc107, #ff9800)',
        error: 'linear-gradient(135deg, #dc3545, #c82333)',
        success: 'linear-gradient(135deg, #28a745, #20c997)'
    };

    toast.style.background = colors[type] || colors.info;
    toast.textContent = message;
    toast.style.opacity = '1';

    setTimeout(() => { toast.style.opacity = '0'; }, 4000);
}

// Enhanced Markdown Renderer
function renderMarkdown(text) {
    if (!text) return '';

    return text
        // Headers
        .replace(/^#### (.*$)/gim, '<h6 class="text-info mt-3 mb-2">$1</h6>')
        .replace(/^### (.*$)/gim, '<h5 class="text-star-blue mt-4 mb-2">$1</h5>')
        .replace(/^## (.*$)/gim, '<h4 class="text-gold mt-4 mb-3">$1</h4>')
        .replace(/^# (.*$)/gim, '<h3 class="text-light mt-4 mb-3">$1</h3>')
        // Bold and Italic
        .replace(/\*\*\*(.*?)\*\*\*/g, '<strong><em>$1</em></strong>')
        .replace(/\*\*(.*?)\*\*/g, '<strong class="text-light">$1</strong>')
        .replace(/\*(.*?)\*/g, '<em>$1</em>')
        // Lists
        .replace(/^- (.*$)/gim, '<div class="ms-3 mb-1">• $1</div>')
        .replace(/^\d+\. (.*$)/gim, '<div class="ms-3 mb-1">$1</div>')
        // Horizontal rules
        .replace(/^---$/gim, '<hr class="border-secondary my-4">')
        .replace(/^___$/gim, '<hr class="border-secondary my-4">')
        // Star ratings (custom)
        .replace(/⭐⭐⭐⭐⭐/g, '<span class="text-warning">★★★★★</span>')
        .replace(/⭐⭐⭐⭐/g, '<span class="text-warning">★★★★☆</span>')
        .replace(/⭐⭐⭐/g, '<span class="text-warning">★★★☆☆</span>')
        .replace(/⭐⭐/g, '<span class="text-warning">★★☆☆☆</span>')
        .replace(/⭐/g, '<span class="text-warning">★☆☆☆☆</span>')
        // Line breaks
        .replace(/\n\n/g, '</p><p class="mb-2">')
        .replace(/\n/g, '<br>');
}

// Loading Animation
function showLoading(element, message = 'Processing...') {
    element.innerHTML = `
        <div class="text-center py-4">
            <div class="spinner-border text-star-blue mb-3" role="status">
                <span class="visually-hidden">Loading...</span>
            </div>
            <p class="text-secondary mb-0">${message}</p>
        </div>
    `;
}

// ISS Tracker
async function fetchISS(city) {
    if (!checkCooldown()) return;
    if (!city || city.trim() === '') {
        showToast('Please enter a city name', 'warning');
        return;
    }

    const resultDiv = document.getElementById('iss-result');
    showLoading(resultDiv, 'Tracking ISS position...');

    try {
        const response = await fetch(`/api/iss?city=${encodeURIComponent(city)}`);
        const data = await response.json();

        if (data.error) {
            resultDiv.innerHTML = `
                <div class="text-center text-danger">
                    <i class="fas fa-exclamation-circle fa-2x mb-2"></i>
                    <p>${data.error}</p>
                </div>`;
            return;
        }

        const colorClass = data.visible ? 'text-success' : 'text-warning';
        const icon = data.visible ? 'fa-check-circle' : 'fa-clock';
        const bgClass = data.visible ? 'border-success' : 'border-warning';

        resultDiv.innerHTML = `
            <div class="text-center ${bgClass} border rounded p-3 mb-3">
                <h3 class="${colorClass}">
                    <i class="fas ${icon} me-2"></i>${data.status_text}
                </h3>
            </div>
            <div class="row text-center">
                <div class="col-md-4 mb-3">
                    <div class="border border-secondary rounded p-3">
                        <i class="fas fa-ruler text-star-blue fa-2x mb-2"></i>
                        <h5 class="text-light mb-0">${data.distance_km.toLocaleString()} km</h5>
                        <small class="text-secondary">Distance</small>
                    </div>
                </div>
                <div class="col-md-4 mb-3">
                    <div class="border border-secondary rounded p-3">
                        <i class="fas fa-map-marker-alt text-star-blue fa-2x mb-2"></i>
                        <h5 class="text-light mb-0">${data.iss_coords.latitude.toFixed(2)}°</h5>
                        <small class="text-secondary">ISS Latitude</small>
                    </div>
                </div>
                <div class="col-md-4 mb-3">
                    <div class="border border-secondary rounded p-3">
                        <i class="fas fa-compass text-star-blue fa-2x mb-2"></i>
                        <h5 class="text-light mb-0">${data.iss_coords.longitude.toFixed(2)}°</h5>
                        <small class="text-secondary">ISS Longitude</small>
                    </div>
                </div>
            </div>
            <p class="text-secondary small text-center mt-2">
                <i class="fas fa-info-circle me-1"></i>
                ISS is visible when within ~1500km, in darkness, and weather permits
            </p>`;

        showToast('ISS location updated!', 'success');
    } catch (e) {
        resultDiv.innerHTML = `
            <div class="text-center text-danger">
                <i class="fas fa-wifi-slash fa-2x mb-2"></i>
                <p>Connection error. Please try again.</p>
            </div>`;
    }
}

// Image Preview Function
function previewImage() {
    const input = document.getElementById('sky-image');
    const preview = document.getElementById('image-preview');
    const previewImg = document.getElementById('preview-img');
    const imageInfo = document.getElementById('image-info');

    if (input.files && input.files[0]) {
        const file = input.files[0];

        // Validate file type
        if (!file.type.match('image.*')) {
            showToast('Please select a valid image file', 'warning');
            return;
        }

        // Validate file size (max 10MB)
        if (file.size > 10 * 1024 * 1024) {
            showToast('Image file size must be less than 10MB', 'warning');
            return;
        }

        const reader = new FileReader();
        reader.onload = function(e) {
            previewImg.src = e.target.result;
            preview.style.display = 'block';

            // Update image info
            const sizeMB = (file.size / (1024 * 1024)).toFixed(2);
            imageInfo.textContent = `${file.name} (${sizeMB} MB) - Ready for analysis`;

            // Scroll to preview
            preview.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
        };
        reader.readAsDataURL(file);
    }
}

// Sky Image Analyzer
async function analyzeImage(input) {
    if (!checkCooldown()) return;
    const file = input.files[0];
    if (!file) {
        showToast('Please select an image first', 'warning');
        return;
    }

    const formData = new FormData();
    formData.append('image', file);

    const resultDiv = document.getElementById('vision-result');
    const btn = document.getElementById('analyze-btn');

    showLoading(resultDiv, 'AI is analyzing your sky image...');
    if (btn) btn.disabled = true;

    try {
        const response = await fetch('/api/analyze', {
            method: 'POST',
            body: formData
        });
        const data = await response.json();

        if (data.error) {
            resultDiv.innerHTML = `
                <div class="text-center text-danger">
                    <i class="fas fa-exclamation-triangle fa-2x mb-2"></i>
                    <p>${data.error}</p>
                </div>`;
            showToast('Analysis failed', 'error');
        } else {
            resultDiv.innerHTML = `
                <div class="text-start text-light">
                    ${renderMarkdown(data.content)}
                </div>`;
            showToast('Analysis complete!', 'success');
        }
    } catch (e) {
        resultDiv.innerHTML = `
            <div class="text-center text-danger">
                <i class="fas fa-exclamation-circle fa-2x mb-2"></i>
                <p>Analysis failed. Please try again.</p>
            </div>`;
        showToast('Connection error', 'error');
    }

    if (btn) btn.disabled = false;
}

// Astronomy Chatbot
async function sendChat() {
    if (!checkCooldown()) return;

    const input = document.getElementById('chat-input');
    const msg = input.value.trim();
    if (!msg) return;

    const chatBox = document.getElementById('chat-box');

    // Add user message
    chatBox.innerHTML += `
        <div class="d-flex justify-content-end mb-3">
            <div class="bg-primary text-white rounded-3 p-3" style="max-width: 75%;">
                <div class="small text-light opacity-75 mb-1">
                    <i class="fas fa-user me-1"></i>You
                </div>
                ${escapeHtml(msg)}
            </div>
        </div>`;
    input.value = '';
    chatBox.scrollTop = chatBox.scrollHeight;

    // Show typing indicator
    const typingId = 'typing-' + Date.now();
    chatBox.innerHTML += `
        <div class="d-flex justify-content-start mb-3" id="${typingId}">
            <div class="bg-dark border border-secondary rounded-3 p-3">
                <span class="spinner-border spinner-border-sm text-star-blue me-2"></span>
                <span class="text-secondary">CosmosAI is thinking...</span>
            </div>
        </div>`;
    chatBox.scrollTop = chatBox.scrollHeight;

    try {
        const response = await fetch('/api/chat', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ message: msg })
        });
        const data = await response.json();

        // Remove typing indicator
        document.getElementById(typingId)?.remove();

        if (data.response) {
            chatBox.innerHTML += `
                <div class="d-flex justify-content-start mb-3">
                    <div class="bg-dark border border-secondary rounded-3 p-3" style="max-width: 85%;">
                        <div class="small text-star-blue mb-2">
                            <i class="fas fa-robot me-1"></i>CosmosAI
                        </div>
                        <div class="text-light">
                            ${renderMarkdown(data.response)}
                        </div>
                    </div>
                </div>`;
        } else {
            chatBox.innerHTML += `
                <div class="d-flex justify-content-start mb-3">
                    <div class="bg-dark border border-danger rounded-3 p-3">
                        <span class="text-danger">
                            <i class="fas fa-exclamation-circle me-1"></i>
                            Unable to get response. Please try again.
                        </span>
                    </div>
                </div>`;
        }
    } catch (e) {
        document.getElementById(typingId)?.remove();
        chatBox.innerHTML += `
            <div class="d-flex justify-content-start mb-3">
                <div class="bg-dark border border-danger rounded-3 p-3">
                    <span class="text-danger">
                        <i class="fas fa-wifi-slash me-1"></i>Connection error
                    </span>
                </div>
            </div>`;
    }
    chatBox.scrollTop = chatBox.scrollHeight;
}

function escapeHtml(text) {
    const div = document.createElement('div');
    div.textContent = text;
    return div.innerHTML;
}

// Dark Sky Location Finder
async function findDarkSky() {
    if (!checkCooldown()) return;

    const cityInput = document.getElementById('city-input');
    const city = cityInput ? cityInput.value.trim() : '';

    if (!city) {
        showToast('Please enter a city name', 'warning');
        return;
    }

    const resultDiv = document.getElementById('dark-sky-result');
    showLoading(resultDiv, `Finding stargazing locations near ${city}...`);

    try {
        const response = await fetch('/api/dark-sky', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ city: city })
        });
        const data = await response.json();

        if (data.error) {
            resultDiv.innerHTML = `
                <div class="text-center text-danger">
                    <i class="fas fa-exclamation-circle fa-2x mb-2"></i>
                    <p>${data.error}</p>
                </div>`;
            showToast('Search failed', 'error');
        } else {
            resultDiv.innerHTML = `
                <div class="text-start">
                    ${renderMarkdown(data.suggestion)}
                </div>`;
            showToast('Locations found!', 'success');
        }
    } catch (e) {
        resultDiv.innerHTML = `
            <div class="text-center text-danger">
                <i class="fas fa-exclamation-circle fa-2x mb-2"></i>
                <p>Error finding locations. Please try again.</p>
            </div>`;
        showToast('Connection error', 'error');
    }
}

// Event Listeners
document.addEventListener('DOMContentLoaded', function () {
    // ISS city input - Enter key
    const issCity = document.getElementById('iss-city');
    if (issCity) {
        issCity.addEventListener('keypress', function (e) {
            if (e.key === 'Enter') fetchISS(this.value);
        });
    }

    // Dark sky city input - Enter key
    const cityInput = document.getElementById('city-input');
    if (cityInput) {
        cityInput.addEventListener('keypress', function (e) {
            if (e.key === 'Enter') findDarkSky();
        });
    }

    // Chat input - Enter key
    const chatInput = document.getElementById('chat-input');
    if (chatInput) {
        chatInput.addEventListener('keypress', function (e) {
            if (e.key === 'Enter' && !e.shiftKey) {
                e.preventDefault();
                sendChat();
            }
        });
    }
});
