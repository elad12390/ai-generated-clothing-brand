import React from 'react';
import { Link } from 'react-router-dom';

const AboutPage = () => {
  return (
    <div className="min-h-screen bg-gray-50">
      {/* Header */}
      <header className="bg-daily-drip-black shadow-sm border-b border-daily-drip-gold">
        <div className="max-w-7xl mx-auto px-4 py-6 sm:px-6 lg:px-8 flex justify-between items-center">
          <h1 className="text-2xl font-bold text-daily-drip-white">The Daily Drip</h1>
          <nav>
            <ul className="flex space-x-6">
              <li><Link to="/" className="text-daily-drip-white hover:text-daily-drip-gold">Home</Link></li>
              <li><Link to="/archive" className="text-daily-drip-white hover:text-daily-drip-gold">Archive</Link></li>
              <li><Link to="/about" className="text-daily-drip-gold font-medium">About</Link></li>
            </ul>
          </nav>
        </div>
      </header>

      {/* Main Content */}
      <main>
        <div className="max-w-7xl mx-auto px-4 py-12 sm:px-6 lg:px-8">
          <div className="lg:text-center mb-16">
            <h1 className="text-3xl font-extrabold text-daily-drip-white sm:text-4xl">
              About The Daily Drip
            </h1>
            <p className="mt-4 max-w-2xl text-xl text-gray-300 lg:mx-auto">
              Where exclusivity meets creativity
            </p>
          </div>

          <div className="prose prose-lg mx-auto text-daily-drip-white">
            <p className="mb-6">
              The Daily Drip is an exclusive fashion collective that creates one-of-a-kind clothing designs each day. Our mysterious creative process combines cutting-edge technology with artistic vision to deliver wearable art that captures the essence of contemporary culture.
            </p>

            <h2 className="text-2xl font-bold text-daily-drip-gold mt-12 mb-6">The Mystery</h2>
            <p className="mb-6">
              What makes each design special isn't just its uniqueness, but the mystery behind its creation. Each day, a new design appears, inspired by the cultural zeitgeist, available for exactly 24 hours before disappearing forever.
            </p>

            <h2 className="text-2xl font-bold text-daily-drip-gold mt-12 mb-6">Our Mission</h2>
            <p className="mb-6">
              We believe that fashion should be both expressive and sustainable. By creating limited-edition designs and using print-on-demand manufacturing, we eliminate waste while celebrating the ever-changing landscape of digital culture. Each piece is a wearable work of art that captures a moment in time.
            </p>

            <h2 className="text-2xl font-bold text-daily-drip-gold mt-12 mb-6">Sustainability</h2>
            <p className="mb-6">
              Traditional fashion contributes significantly to environmental pollution through overproduction and waste. Our model is different:
            </p>
            <ul className="list-disc pl-6 mb-6 space-y-2 text-gray-300">
              <li>No inventory is produced until an order is placed</li>
              <li>Only designs that are purchased are manufactured</li>
              <li>We use eco-friendly inks and sustainable materials whenever possible</li>
              <li>Our packaging is minimal and recyclable</li>
            </ul>

            <h2 className="text-2xl font-bold text-daily-drip-gold mt-12 mb-6">Our Network</h2>
            <p className="mb-6">
              We've partnered with industry leaders to ensure the highest quality production and fulfillment of our designs.
            </p>

            <h2 className="text-2xl font-bold text-daily-drip-gold mt-12 mb-6">Join the Movement</h2>
            <p>
              Be part of an exclusive community that values creativity and scarcity. Follow us on social media to stay updated on daily releases, and don't forget to showcase your drip with the hashtag #TheDailyDrip.
            </p>
          </div>

          <div className="mt-16 bg-daily-drip-gold rounded-lg p-8 text-center">
            <h2 className="text-2xl font-bold text-daily-drip-black mb-4">Ready to Experience Tomorrow's Drip Today?</h2>
            <p className="text-lg text-daily-drip-black mb-6">
              Visit our homepage to see today's exclusive design
            </p>
            <Link 
              to="/" 
              className="inline-block daily-drip-button px-6 py-3 rounded-md font-medium hover:bg-daily-drip-gold focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-daily-drip-gold"
            >
              View Today's Drip
            </Link>
          </div>
        </div>
      </main>

      {/* Footer */}
      <footer className="bg-gray-800">
        <div className="max-w-7xl mx-auto py-12 px-4 sm:px-6 lg:px-8">
          <div className="md:flex md:items-center md:justify-between">
            <div className="flex justify-center md:justify-start">
              <p className="text-gray-300">AI Generated Clothing Brand</p>
            </div>
            <div className="mt-8 md:mt-0 flex justify-center md:justify-end">
              <p className="text-gray-300">Powered by AI & Print-on-Demand</p>
            </div>
          </div>
          <div className="mt-8 border-t border-gray-700 pt-8 md:flex md:items-center md:justify-between">
            <div className="flex space-x-6 md:order-2 justify-center">
              <a href="#" className="text-gray-400 hover:text-gray-300">
                <span className="sr-only">Twitter</span>
                <svg className="h-6 w-6" fill="currentColor" viewBox="0 0 24 24" aria-hidden="true">
                  <path d="M8.29 20.251c7.547 0 11.675-6.253 11.675-11.675 0-.178 0-.355-.012-.53A8.348 8.348 0 0022 5.92a8.19 8.19 0 01-2.357.646 4.118 4.118 0 001.804-2.27 8.224 8.224 0 01-2.605.996 4.107 4.107 0 00-6.993 3.743 11.65 11.65 0 01-8.457-4.287 4.106 4.106 0 001.27 5.477A4.072 4.072 0 012.8 9.713v.052a4.105 4.105 0 003.292 4.022 4.095 4.095 0 01-1.853.07 4.108 4.108 0 003.834 2.85A8.233 8.233 0 012 18.407a11.616 11.616 0 006.29 1.84"></path>
                </svg>
              </a>
              <a href="#" className="text-gray-400 hover:text-gray-300">
                <span className="sr-only">Instagram</span>
                <svg className="h-6 w-6" fill="currentColor" viewBox="0 0 24 24" aria-hidden="true">
                  <path fillRule="evenodd" d="M12.315 2c2.43 0 2.784.013 3.808.06 1.064.049 1.791.218 2.427.465a4.902 4.902 0 011.772 1.153 4.902 4.902 0 011.153 1.772c.247.636.416 1.363.465 2.427.048 1.067.06 1.407.06 4.123v.08c0 2.643-.012 2.987-.06 4.043-.049 1.064-.218 1.791-.465 2.427a4.902 4.902 0 01-1.153 1.772 4.902 4.902 0 01-1.772 1.153c-.636.247-1.363.416-2.427.465-1.067.048-1.407.06-4.123.06h-.08c-2.643 0-2.987-.012-4.043-.06-1.064-.049-1.791-.218-2.427-.465a4.902 4.902 0 01-1.772-1.153 4.902 4.902 0 01-1.153-1.772c-.247-.636-.416-1.363-.465-2.427-.047-1.024-.06-1.379-.06-3.808v-.63c0-2.43.013-2.784.06-3.808.049-1.064.218-1.791.465-2.427a4.902 4.902 0 011.153-1.772A4.902 4.902 0 015.45 2.525c.636-.247 1.363-.416 2.427-.465C8.901 2.013 9.256 2 11.685 2h.63zm-.081 1.802h-.468c-2.456 0-2.784.011-3.807.058-.975.045-1.504.207-1.857.344-.467.182-.8.398-1.15.748-.35.35-.566.683-.748 1.15-.137.353-.3.882-.344 1.857-.047 1.023-.058 1.351-.058 3.807v.468c0 2.456.011 2.784.058 3.807.045.975.207 1.504.344 1.857.182.466.399.8.748 1.15.35.35.683.566 1.15.748.353.137.882.3 1.857.344 1.054.048 1.37.058 4.041.058h.08c2.597 0 2.917-.01 3.96-.058.976-.045 1.505-.207 1.858-.344.466-.182.8-.398 1.15-.748.35-.35.566-.683.748-1.15.137-.353.3-.882.344-1.857.048-1.055.058-1.37.058-4.041v-.08c0-2.597-.01-2.917-.058-3.96-.045-.976-.207-1.505-.344-1.858a3.097 3.097 0 00-.748-1.15 3.098 3.098 0 00-1.15-.748c-.353-.137-.882-.3-1.857-.344-1.023-.047-1.351-.058-3.807-.058zM12 6.865a5.135 5.135 0 110 10.27 5.135 5.135 0 010-10.27zm0 1.802a3.333 3.333 0 100 6.666 3.333 3.333 0 000-6.666zm5.338-3.205a1.2 1.2 0 110 2.4 1.2 1.2 0 010-2.4z" clipRule="evenodd"></path>
                </svg>
              </a>
            </div>
            <div className="mt-8 md:mt-0 md:order-1">
              <p className="text-center text-base text-gray-400">
                &copy; 2025 The Daily Drip. All rights reserved.
              </p>
            </div>
          </div>
        </div>
      </footer>
    </div>
  );
};

export default AboutPage;