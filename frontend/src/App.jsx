import React, { useState } from 'react';
import UrlInput from './components/UrlInput';
import ReportView from './components/ReportView';
import LoadingSpinner from './components/LoadingSpinner';
import './App.css';

function App() {
  const [report, setReport] = useState(null);
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState(null);

  const handleScrape = async (url) => {
    setIsLoading(true);
    setError(null);
    setReport(null);

    try {
      const response = await fetch('http://localhost:8000/scrape', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ url }),
      });

      if (!response.ok) {
        const errorData = await response.json();
        throw new Error(errorData.detail || 'Failed to analyze website');
      }

      const data = await response.json();
      setReport(data.report);
    } catch (err) {
      setError(err.message);
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <div className="app-container">
      <header className="app-header">
        <h1>AI Web Scraper</h1>
        <p>Enter a URL to generate a detailed AI analysis report.</p>
      </header>

      <main className="app-main">
        <UrlInput onScrape={handleScrape} isLoading={isLoading} />

        {error && <div className="error-message glass-panel">{error}</div>}

        {isLoading && <LoadingSpinner />}

        {report && <ReportView report={report} />}
      </main>

      <footer className="app-footer">
        <p>Powered by Gemini & Playwright</p>
      </footer>
    </div>
  );
}

export default App;
