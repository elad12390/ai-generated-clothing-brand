// API service for communicating with the backend
const API_BASE_URL = 'http://localhost:8000/api';

// Get the daily shirt design
export const getDailyShirt = async () => {
  try {
    const response = await fetch(`${API_BASE_URL}/daily-shirt`);
    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`);
    }
    return await response.json();
  } catch (error) {
    console.error('Error fetching daily shirt:', error);
    // Return mock data in case of error
    return {
      id: 1,
      topic: "AI Technology",
      imageUrl: "https://placehold.co/600x600/2563eb/white?text=AI+Technology+Shirt",
      createdAt: new Date().toISOString(),
      description: "Today's exclusive AI-generated design featuring AI Technology"
    };
  }
};

// Get all shirt designs for the archive
export const getShirtArchive = async () => {
  try {
    const response = await fetch(`${API_BASE_URL}/shirts`);
    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`);
    }
    return await response.json();
  } catch (error) {
    console.error('Error fetching shirt archive:', error);
    // Return mock data in case of error
    return [
      {
        id: 1,
        topic: "Machine Learning",
        imageUrl: "https://placehold.co/300x300/8b5cf6/white?text=ML+Shirt",
        createdAt: new Date(Date.now() - 86400000).toISOString(), // Yesterday
      },
      {
        id: 2,
        topic: "Neural Networks",
        imageUrl: "https://placehold.co/300x300/0ea5e9/white?text=NN+Shirt",
        createdAt: new Date(Date.now() - 2 * 86400000).toISOString(), // 2 days ago
      },
      {
        id: 3,
        topic: "Data Science",
        imageUrl: "https://placehold.co/300x300/10b981/white?text=DS+Shirt",
        createdAt: new Date(Date.now() - 3 * 86400000).toISOString(), // 3 days ago
      },
      {
        id: 4,
        topic: "Cloud Computing",
        imageUrl: "https://placehold.co/300x300/f97316/white?text=CC+Shirt",
        createdAt: new Date(Date.now() - 4 * 86400000).toISOString(), // 4 days ago
      },
      {
        id: 5,
        topic: "Cybersecurity",
        imageUrl: "https://placehold.co/300x300/ef4444/white?text=CS+Shirt",
        createdAt: new Date(Date.now() - 5 * 86400000).toISOString(), // 5 days ago
      },
      {
        id: 6,
        topic: "Blockchain",
        imageUrl: "https://placehold.co/300x300/06b6d4/white?text=BC+Shirt",
        createdAt: new Date(Date.now() - 6 * 86400000).toISOString(), // 6 days ago
      },
    ];
  }
};