/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./templates/**/*.html",
    "./static/css/**/*.css",
  ],
  theme: {
    extend: {
      fontFamily: {
        Roboto: ["Roboto", "serif"],
      },
    },
  },
  plugins: [],
}

