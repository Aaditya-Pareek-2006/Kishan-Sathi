// frontend/component.js
function createPriceCard(data) {
    const borderClass = data.isPrivate ? "border-l-4 border-l-blue-500 border-blue-100" : "border-gray-100";
    const verifiedBadge = data.isVerified ? `<i class="fa-solid fa-circle-check text-blue-500 text-xs" title="Verified Buyer"></i>` : '';
    const locationIcon = data.isPrivate ? `<i class="fa-solid fa-star text-yellow-400"></i> ${data.trustScore} Trust Score` : `<i class="fa-solid fa-location-dot text-red-400"></i> ${data.distance} km door`;
    const extraInfo = data.isPrivate ? `<p class="text-xs text-blue-600 font-medium flex items-center justify-end gap-1 mt-0.5 bg-blue-50 px-1.5 py-0.5 rounded"><i class="fa-solid fa-warehouse"></i> Farm Pickup</p>` : `<p class="text-xs text-red-500 font-medium flex items-center justify-end gap-1 mt-0.5"><i class="fa-solid fa-truck"></i> -₹${data.transportCost} (Kiraya)</p>`;

    return `
        <article tabindex="0" class="bg-white p-4 rounded-xl shadow-sm border flex justify-between items-center hover:shadow-md transition-shadow cursor-pointer relative overflow-hidden focus:outline-none focus:ring-2 focus:ring-green-300 mb-3 ${borderClass}">
            <div class="flex items-start gap-3">
                <div class="${data.isPrivate ? 'bg-blue-100 text-blue-600' : 'bg-orange-100 text-orange-600'} p-2 rounded-lg mt-1">
                    <i class="fa-solid ${data.isPrivate ? 'fa-handshake' : 'fa-building-columns'}"></i>
                </div>
                <div>
                    <h4 class="font-bold text-gray-800 flex items-center gap-1">${data.buyerName} ${verifiedBadge}</h4>
                    <p class="text-xs text-gray-500 mt-0.5">${locationIcon}</p>
                </div>
            </div>
            <div class="text-right">
                <p class="text-lg font-bold ${data.isPrivate ? 'text-green-600' : 'text-gray-800'}"><span class="live-indicator"></span>₹${data.price} <span class="text-xs text-gray-500 font-normal">/qtl</span></p>
                ${extraInfo}
            </div>
        </article>
    `;
}