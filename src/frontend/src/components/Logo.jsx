import React from 'react';
import logo from '../assets/logo.png';

const Logo = ({ size = 'default', className = '' }) => {
  const sizeClasses = {
    small: 'h-8 w-auto',
    default: 'h-12 w-auto',
    large: 'h-16 w-auto',
    xl: 'h-20 w-auto'
  };

  return (
    <img 
      src={logo} 
      alt="The Daily Drip Logo" 
      className={`${sizeClasses[size]} ${className}`}
    />
  );
};

export default Logo;