import React from 'react';

const ProductDetailsModal = ({ shirt, isOpen, onClose }) => {
  if (!isOpen) return null;

  return (
    <div className="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center z-50 p-4">
      <div className="bg-white rounded-lg max-w-2xl w-full max-h-[90vh] overflow-y-auto">
        <div className="p-6">
          <div className="flex justify-between items-start">
            <h2 className="text-2xl font-bold text-gray-900">Product Details</h2>
            <button 
              onClick={onClose}
              className="text-gray-400 hover:text-gray-500 text-2xl font-bold"
            >
              &times;
            </button>
          </div>
          <div className="mt-4">
            <h3 className="text-xl font-semibold text-gray-900">{shirt?.topic}</h3>
          
          <div className="mt-4">
            <img 
              src={shirt?.imageUrl} 
              alt={shirt?.topic} 
              className="w-full h-auto rounded-lg"
            />
          </div>
          
          <div className="mt-6">
            <div className="flex justify-between items-center">
              <div>
                <p className="text-sm text-gray-500">Release Date</p>
                <p className="font-medium">{new Date(shirt?.createdAt).toLocaleDateString()}</p>
              </div>
              <span className="inline-flex items-center px-3 py-1 rounded-full text-sm font-medium bg-red-100 text-red-800">
                Limited Edition
              </span>
            </div>
            
            <div className="mt-6">
              <h3 className="text-lg font-medium text-gray-900">About this design</h3>
              <p className="mt-2 text-gray-600">
                {shirt?.description || "An exclusive AI-generated design featuring today's trending topic."}
              </p>
            </div>
            
            <div className="mt-6">
              <h3 className="text-lg font-medium text-gray-900">QR Code</h3>
              <div className="mt-2 flex items-center justify-center p-4 bg-gray-100 rounded-lg">
                <div className="bg-white p-2 rounded">
                  <img 
                    src="https://placehold.co/150x150/000000/white?text=QR+Code" 
                    alt="QR Code" 
                    className="w-32 h-32"
                  />
                </div>
              </div>
              <p className="mt-2 text-sm text-gray-500 text-center">
                Scan to purchase this limited edition design
              </p>
            </div>
            
            <div className="mt-8 flex space-x-4">
              <button className="flex-1 bg-indigo-600 text-white py-3 px-4 rounded-md font-medium hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500">
                Buy Now
              </button>
              <button className="flex-1 bg-white border border-gray-300 text-gray-700 py-3 px-4 rounded-md font-medium hover:bg-gray-50 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500">
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