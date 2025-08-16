import React from 'react';
import { Link } from 'react-router-dom';

const NotFoundPage = () => {
  return (
    <div className="min-h-screen bg-daily-drip-black flex items-center justify-center">
      <div className="max-w-md w-full text-center">
        <h1 className="text-6xl font-extrabold text-daily-drip-white mb-4">404</h1>
        <h2 className="text-2xl font-bold text-daily-drip-gold mb-4">Drip Not Found</h2>
        <p className="text-lg text-gray-300 mb-8">
          Sorry, we couldn't find the drip you're looking for.
        </p>
        <Link 
          to="/" 
          className="inline-block daily-drip-button px-6 py-3 rounded-md font-medium hover:bg-daily-drip-gold focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-daily-drip-gold"
        >
          Go back to the drip
        </Link>
      </div>
    </div>
  );
};

export default NotFoundPage;