// frontend/speedometerGauge.js
function createAIGauge(predictionData) {
    const isSell = predictionData.action === "SELL";
    const bgColor = isSell ? "bg-green-100" : "bg-red-100";
    const textColor = isSell ? "text-green-700" : "text-red-700";
    const icon = isSell ? `<i class="fa-solid fa-arrow-trend-up animate-bounce"></i>` : `<i class="fa-solid fa-hand"></i>`;
    const actionText = isSell ? "Abhi Bechein (Sell Now)" : "Rukein (Hold)";
    const gaugeWidth = isSell ? "w-[85%]" : "w-[25%]";
    const gaugeColor = isSell ? "bg-green-500" : "bg-red-500";

    return `
        <div class="text-center">
            <div class="inline-block px-6 py-3 rounded-full ${bgColor} ${textColor} font-bold text-xl flex items-center gap-2 justify-center mx-auto w-max shadow-sm border border-opacity-50">
                ${icon} ${actionText}
            </div>
            <div class="w-full bg-gray-200 rounded-full h-2 mt-4 overflow-hidden shadow-inner">
                <div class="${gaugeColor} h-2 rounded-full ${gaugeWidth} transition-all duration-1000 ease-in-out"></div>
            </div>
            <p class="text-[10px] text-gray-400 mt-1.5 font-medium uppercase tracking-wider">AI Confidence: ${predictionData.confidence}</p>
        </div>
    `;
}