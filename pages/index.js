// Assuming Label and Button are components that accept className props
import React from 'react';
import { Label } from "@/components/ui/label";
import Button from "@/components/ui/button";
import styles from '../styles/index.module.css';

export default function Component() {
  return (
    <div className={styles.container}>
      <div className={styles.pdfPreview}>
        <h2 className={styles.pdfTitle}>PDF Placeholder</h2>
        <div className={styles.pdfContainer}>
          <img
            alt="PDF Preview"
            className={styles.pdfImage}
            src="/placeholder.svg"
          />
        </div>
      </div>
      <div className={styles.querySection}>
        <div className={styles.textCenter}>
          <Label className={styles.label} htmlFor="voice">
            Click to start dictation
          </Label>
          <div className={styles.inputContainer}>
            <input
              className={styles.voiceInput}
              id="voice"
              placeholder="Try saying: What's on your mind?"
              type="text"
            />
          </div>
        </div>
        <Button className={styles.button}>
          <MicIcon className={styles.micIcon} />
          Start Voice
        </Button>
        <a className={styles.pdfExport} href="#">
          Export as PDF
        </a>
      </div>
    </div>
  );
}

function MicIcon(props) {
  // Ensure the styles.micIcon is defined in your CSS module to apply styles to MicIcon
  return (
    <svg
      {...props}
      className={styles.micIcon}
      xmlns="http://www.w3.org/2000/svg"
      width="24"
      height="24"
      viewBox="0 0 24 24"
      fill="none"
      stroke="currentColor"
      strokeWidth="2"
      strokeLinecap="round"
      strokeLinejoin="round"
    >
      <path d="M12 2a3 3 0 0 0-3 3v7a3 3 0 0 0 6 0V5a3 3 0 0 0-3-3Z" />
      <path d="M19 10v2a7 7 0 0 1-14 0v-2" />
      <line x1="12" x2="12" y1="19" y2="22" />
    </svg>
  );
}
