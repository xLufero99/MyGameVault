export const games = [
  {
    id: 1,
    title: "Elden Ring",
    cover: "https://images.unsplash.com/photo-1518709268805-4e9042af9f23?w=300&h=420&fit=crop&auto=format",
    genre: ["Action RPG", "Open World"],
    platform: ["PC", "PS5", "Xbox Series X", "PS4"],
    developer: "FromSoftware",
    publisher: "Bandai Namco",
    year: 2022,
    score: 9.5,
    userScore: 9,
    members: 1234567,
    ranked: 2,
    description: "Rise, Tarnished...",
    tags: ["Open World", "Difficult", "Dark Fantasy", "Co-op", "Exploration"],
    status: 'completed',
    hours: 120,
  },
  // ... el resto de juegos
];
export const topRanked = [...games].sort((a, b) => b.score - a.score);
export const recentGames = [...games].sort((a, b) => b.year - a.year);
export const mockReviews = [ /* ... */ ];
export const userProfile = { /* ... */ };