// frontend/app.js

const mockData = {
    crop: "Pyaz (Onion)",
    mandiPrice: 1200,
    transportCost: 100,
    privatePrice: 1350,
    privateBuyerName: "AgriFresh Co.",
    trustScore: 4.8,
    aiPrediction: { action: "SELL", confidence: "85%", reason: "Mock: Kal mandi me supply badhne wali hai." }
};

window.showToast = function(message, type) {
    const toastContainer = document.getElementById('toast-container');
    if (!toastContainer) return;
    const toast = document.createElement('div');
    toast.className = `p-3 rounded shadow-md text-white text-sm font-bold ${type === 'success' ? 'bg-green-500' : 'bg-blue-500'} animate-fade-in-up`;
    toast.innerText = message;
    toastContainer.appendChild(toast);
    setTimeout(() => { toast.style.opacity = '0';
        setTimeout(() => toast.remove(), 300); }, 3000);
};

window.retryFetch = function() {
    window.showToast("Retrying...", "info");
    document.dispatchEvent(new Event('fetchDataAgain'));
};

document.addEventListener("DOMContentLoaded", () => {
    const aiMeterContainer = document.querySelector('#ai-meter-container');
    const langBtn = document.querySelector('#lang-toggle');

    // Live Fetch API
    async function fetchLiveMandiData() {
        try {
            if (aiMeterContainer) aiMeterContainer.innerHTML = '<p class="text-center text-gray-500 animate-pulse">AI Data load kar raha hai...</p>';

            // Backend call
            const response = await fetch('http://127.0.0.1:8000/api/dashboard-data?crop=Pyaz&farmer_lat=27.86&farmer_lon=75.38');
            if (!response.ok) throw new Error(`Server error!`);

            const realData = await response.json();
            document.getElementById('api-error-banner').classList.add('hidden');
            updateDashboard(realData);
            window.showToast("Live AI Data Synced! 🚀", "success");

        } catch (error) {
            console.error("Backend connect nahi hua:", error);
            document.getElementById('api-error-banner').classList.remove('hidden'); // Yahi banner tumhe dikh raha hai
            updateDashboard(mockData); // Fail-safe (Banner ke sath mock data dikhayega)
        }
    }

    if (aiMeterContainer) fetchLiveMandiData();
    document.addEventListener('fetchDataAgain', fetchLiveMandiData);

    // Language Toggle (i18n)
    let isHindi = true;
    if (langBtn) {
        langBtn.addEventListener('click', () => {
            isHindi = !isHindi;
            document.getElementById('current-lang').innerText = isHindi ? "HI" : "EN";
            const mainHeading = document.querySelector('h2.text-lg.font-bold');
            if (mainHeading) mainHeading.innerHTML = isHindi ? 'Mandi Bhav <span class="text-green-600">(Pyaz)</span>' : 'Market Rates <span class="text-green-600">(Onion)</span>';
            window.showToast(isHindi ? "🌐 Bhasha Hindi set ho gayi." : "🌐 Language switched to English.", "info");
        });
    }
});

function updateDashboard(data) {
    const aiMeterContainer = document.querySelector('#ai-meter-container');
    if (aiMeterContainer && typeof createAIGauge === 'function') {
        aiMeterContainer.innerHTML = `<div class="flex items-center justify-center gap-2 mb-3"><i class="fa-solid fa-robot text-green-600"></i><p class="text-sm text-gray-600 font-bold uppercase tracking-wide">AI Fasal Salah</p></div>` +
            createAIGauge(data.aiPrediction) +
            `<div class="mt-4 bg-white p-3 rounded-md shadow-sm text-left border-l-2 ${data.aiPrediction.action === 'SELL' ? 'border-green-400' : 'border-red-400'}"><p class="text-sm text-gray-700 font-medium"><i class="fa-solid fa-circle-info ${data.aiPrediction.action === 'SELL' ? 'text-green-500' : 'text-red-500'} mr-1"></i> Alert:</p><p class="text-xs text-gray-500 mt-1">${data.aiPrediction.reason}</p></div>`;
    }

    const buyerListContainer = document.querySelector('#market-list');
    if (buyerListContainer && typeof createPriceCard === 'function') {
        buyerListContainer.innerHTML = createPriceCard({ buyerName: "Jhunjhunu Mandi", price: data.mandiPrice, distance: data.mandiDistanceKm, transportCost: data.transportCost, isPrivate: false, isVerified: true }) +
            createPriceCard({ buyerName: data.privateBuyerName, price: data.privatePrice, isPrivate: true, isVerified: true, trustScore: data.trustScore });
    }
}