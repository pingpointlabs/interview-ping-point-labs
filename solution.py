"""
PingPoint Labs - Door Schedule Extraction Solution

Your task: Extract door schedule information from a construction PDF
and output it in a structured format (CSV or JSON).
"""

import fitz  # PyMuPDF
import pandas as pd
from pathlib import Path


def download_pdf(url: str, output_path: str = "construction_drawing.pdf") -> str:
    """
    Download PDF from URL.

    Args:
        url: URL to the PDF document
        output_path: Local path to save the PDF

    Returns:
        Path to the downloaded PDF file
    """
    # TODO: Implement PDF download logic
    # You can use urllib, requests, or any other method
    pass


def extract_door_schedule(pdf_path: str) -> pd.DataFrame:
    """
    Extract door schedule from PDF.

    Args:
        pdf_path: Path to the PDF file

    Returns:
        DataFrame with door schedule data containing columns:
        - Door Mark (e.g., "101", "102A")
        - Door Size (e.g., "3-0 x 7-0")
        - Door Material/Type (e.g., "HM", "Wood")
        - Fire Rating (if applicable)
        - Hardware Set (e.g., "HS-1", "HS-2")
    """
    # TODO: Implement extraction logic

    # Example structure to get you started:
    doc = fitz.open(pdf_path)

    # Your extraction logic here
    # Hint: You might want to:
    # 1. Find the page with the door schedule
    # 2. Extract text or tables from that page
    # 3. Parse the extracted data into structured format

    doc.close()

    # Return a DataFrame with the extracted data
    return pd.DataFrame()


def save_output(df: pd.DataFrame, output_dir: str = "output") -> None:
    """
    Save extracted data to output directory.

    Args:
        df: DataFrame with door schedule data
        output_dir: Directory to save output files
    """
    Path(output_dir).mkdir(exist_ok=True)

    # Save as CSV
    csv_path = Path(output_dir) / "door_schedule.csv"
    df.to_csv(csv_path, index=False)
    print(f"✅ Saved CSV to {csv_path}")

    # Save as JSON
    json_path = Path(output_dir) / "door_schedule.json"
    df.to_json(json_path, orient="records", indent=2)
    print(f"✅ Saved JSON to {json_path}")


def main():
    """Main execution function."""
    # PDF URL will be provided during the interview
    pdf_url = "YOUR_PDF_URL_HERE"

    # Step 1: Download or load PDF
    # pdf_path = download_pdf(pdf_url)
    pdf_path = "construction_drawing.pdf"  # Or use direct path

    # Step 2: Extract door schedule
    print("Extracting door schedule...")
    door_schedule = extract_door_schedule(pdf_path)

    # Step 3: Display results
    print(f"\nExtracted {len(door_schedule)} doors")
    print(door_schedule.head())

    # Step 4: Save output
    save_output(door_schedule)

    print("\n✅ Extraction complete!")


if __name__ == "__main__":
    main()
