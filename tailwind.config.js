/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./index.html",
    "./merci.html",
    "./articles/**/*.html",
  ],
  theme: {
    extend: {
      colors: {
        primary: '#1D4ED8',
        secondary: '#F59E0B',
        dark: '#1F2937',
        light: '#F3F4F6',
      }
    }
  },
  plugins: [],
}
