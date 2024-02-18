// pages/_app.js
import '../styles/globals.css'; // Adjust the path if your file structure is different

function MyApp({ Component, pageProps }) {
  return <Component {...pageProps} />;
}

export default MyApp;
