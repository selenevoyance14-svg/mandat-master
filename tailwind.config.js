/** @type {import('tailwindcss').Config} */
module.exports = {
    content: [
        './src/pages/**/*.{js,ts,jsx,tsx,mdx}',
        './src/components/**/*.{js,ts,jsx,tsx,mdx}',
        './src/app/**/*.{js,ts,jsx,tsx,mdx}',
    ],
    theme: {
        extend: {
            colors: {
                primary: '#1D4ED8', // Royal Blue
                secondary: '#F59E0B', // Amber
                dark: '#1F2937',
                light: '#F3F4F6',
            },
        },
    },
    plugins: [],
}
