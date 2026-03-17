import asyncio
from playwright.async_api import async_playwright
import os

async def generate_pdf():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()
        
        # Path to local HTML
        html_path = "file:///C:/Users/PC/OneDrive/Documents/WORKSPACE/HoangMinhCV/cv_v2.html"
        await page.goto(html_path, wait_until="networkidle")
        
        # Wait a bit longer to ensure external fonts and icons load
        await page.wait_for_timeout(2000)
        
        # Generate PDF targeting exactly A4 with no margins and retaining background
        await page.pdf(
            path="HoangMinh_CV_v2_final2.pdf",
            format="A4",
            print_background=True,
            margin={"top": "0", "right": "0", "bottom": "0", "left": "0"}
        )
        await browser.close()
        print("Successfully exported HoangMinh_CV_v2_final2.pdf")

if __name__ == "__main__":
    asyncio.run(generate_pdf())
