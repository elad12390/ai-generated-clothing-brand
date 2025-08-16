import React from 'react';

const ProductDetailsModal = ({ shirt, isOpen, onClose }) => {
  if (!isOpen) return null;

  return (
    <div className="fixed inset-0 bg-daily-drip-black bg-opacity-90 flex items-center justify-center z-50 p-4">
      <div className="bg-daily-drip-white rounded-lg max-w-2xl w-full max-h-[90vh] overflow-y-auto border border-daily-drip-gold">
        <div className="p-6">
          <div className="flex justify-between items-start">
            <h2 className="text-2xl font-bold text-daily-drip-black">Product Details</h2>
            <button 
              onClick={onClose}
              className="text-daily-drip-black hover:text-daily-drip-gold text-2xl font-bold"
            >
              &times;
            </button>
          </div>
          <div className="mt-4">
            <h3 className="text-xl font-semibold text-daily-drip-black">{shirt?.topic}</h3>
          </div>
          
          <div className="mt-4">
            <img 
              src={shirt?.imageUrl} 
              alt={shirt?.topic} 
              className="w-full h-auto rounded-lg border border-daily-drip-gold"
            />
          </div>
          
          <div className="mt-6">
            <div className="flex justify-between items-center">
              <div>
                <p className="text-sm text-gray-600">Release Date</p>
                <p className="font-medium text-daily-drip-black">{new Date(shirt?.createdAt).toLocaleDateString()}</p>
              </div>
              <span className="inline-flex items-center px-3 py-1 rounded-full text-sm font-medium bg-daily-drip-gold text-daily-drip-black">
                Limited Edition
              </span>
            </div>
            
            <div className="mt-6">
              <h3 className="text-lg font-medium text-daily-drip-black">About this design</h3>
              <p className="mt-2 text-gray-700">
                {shirt?.description || "An exclusive design featuring today's inspiration."}
              </p>
            </div>
            
            <div className="mt-6">
              <h3 className="text-lg font-medium text-daily-drip-black">QR Code</h3>
              <div className="mt-2 flex items-center justify-center p-4 bg-daily-drip-black rounded-lg">
                <div className="bg-white p-2 rounded border border-daily-drip-gold">
                  <img 
                    src="https://placehold.co/150x150/000000/white?text=QR+Code" 
                    alt="QR Code" 
                    className="w-32 h-32"
                  />
                </div>
              </div>
              <p className="mt-2 text-sm text-gray-600 text-center">
                Scan to purchase this limited edition design
              </p>
            </div>
            
            <div className="mt-8 flex space-x-4">
              <button className="flex-1 daily-drip-button py-3 px-4 rounded-md font-medium focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-daily-drip-gold">
                Buy Now
              </button>
              <button className="flex-1 daily-drip-button-secondary py-3 px-4 rounded-md font-medium focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-daily-drip-gold">
                Share
              </button>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default ProductDetailsModal;