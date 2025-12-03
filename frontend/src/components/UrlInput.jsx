import React, { useState } from 'react';
import './UrlInput.css';

const UrlInput = ({ onScrape, isLoading }) => {
    const [url, setUrl] = useState('');

    const handleSubmit = (e) => {
        e.preventDefault();
        if (url) {
            onScrape(url);
        }
    };

    return (
        <div className="url-input-container glass-panel">
            <form onSubmit={handleSubmit} className="url-form">
                <input
                    type="url"
                    placeholder="Paste website URL here..."
                    value={url}
                    onChange={(e) => setUrl(e.target.value)}
                    required
                    className="url-input"
                    disabled={isLoading}
                />
                <button type="submit" className="scrape-button" disabled={isLoading}>
                    {isLoading ? 'Analyzing...' : 'Analyze'}
                </button>
            </form>
        </div>
    );
};

export default UrlInput;
