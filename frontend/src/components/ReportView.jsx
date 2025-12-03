import React from 'react';
import ReactMarkdown from 'react-markdown';
import './ReportView.css';

const ReportView = ({ report }) => {
    if (!report) return null;

    const handleDownload = () => {
        const blob = new Blob([report], { type: 'text/markdown' });
        const url = URL.createObjectURL(blob);
        const a = document.createElement('a');
        a.href = url;
        a.download = 'website_analysis_report.md';
        document.body.appendChild(a);
        a.click();
        document.body.removeChild(a);
        URL.revokeObjectURL(url);
    };

    return (
        <div className="report-container glass-panel">
            <div className="report-header">
                <h2>Analysis Report</h2>
                <button onClick={handleDownload} className="download-button">
                    Download Report
                </button>
            </div>
            <div className="report-content">
                <ReactMarkdown>{report}</ReactMarkdown>
            </div>
        </div>
    );
};

export default ReportView;
