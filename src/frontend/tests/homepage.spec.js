// tests/homepage.spec.js
import { test, expect } from '@playwright/test';

test('homepage has title and daily shirt display', async ({ page }) => {
  await page.goto('/');

  // Expect the page title to contain "AI Generated Clothing"
  await expect(page).toHaveTitle(/AI Generated Clothing/);

  // Expect the main heading to be visible
  await expect(page.getByText('Today\'s Exclusive')).toBeVisible();

  // Expect the daily shirt image to be visible
  await expect(page.getByAltText('AI Technology')).toBeVisible();

  // Expect the countdown timer to be visible
  await expect(page.getByText('Next release in')).toBeVisible();

  // Expect the "View Details" button to be visible
  await expect(page.getByRole('button', { name: 'View Details' })).toBeVisible();
});

test('navigation works correctly', async ({ page }) => {
  await page.goto('/');

  // Click on the Archive link
  await page.click('text=Archive');
  
  // Expect to be on the archive page
  await expect(page).toHaveURL(/.*archive/);
  await expect(page.getByText('Design Archive')).toBeVisible();

  // Click on the About link
  await page.click('text=About');
  
  // Expect to be on the about page
  await expect(page).toHaveURL(/.*about/);
  await expect(page.getByText('About AI Generated Clothing')).toBeVisible();

  // Click on the Home link
  await page.click('text=Home');
  
  // Expect to be back on the home page
  await expect(page).toHaveURL('/');
  await expect(page.getByText('Today\'s Exclusive')).toBeVisible();
});

test('product details modal opens and closes', async ({ page }) => {
  await page.goto('/');

  // Click the "View Details" button
  await page.click('button:has-text("View Details")');

  // Expect the modal to be visible
  await expect(page.getByText('Product Details')).toBeVisible();

  // Click the close button
  await page.click('button:has-text("×")');

  // Expect the modal to be closed
  await expect(page.getByText('Product Details')).not.toBeVisible();
});