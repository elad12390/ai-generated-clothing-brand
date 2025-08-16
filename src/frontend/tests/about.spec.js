// tests/about.spec.js
import { test, expect } from '@playwright/test';

test('about page displays correct content', async ({ page }) => {
  await page.goto('/about');

  // Expect the page title to contain "AI Generated Clothing"
  await expect(page).toHaveTitle(/AI Generated Clothing/);

  // Expect the about heading to be visible
  await expect(page.getByText('About AI Generated Clothing')).toBeVisible();

  // Expect to see information about how it works
  await expect(page.getByText('How It Works')).toBeVisible();

  // Expect to see information about the mission
  await expect(page.getByText('Our Mission')).toBeVisible();

  // Expect to see information about sustainability
  await expect(page.getByText('Sustainability')).toBeVisible();
});

test('about page navigation works', async ({ page }) => {
  await page.goto('/about');

  // Click on the Home link
  await page.click('text=Home');
  
  // Expect to be on the home page
  await expect(page).toHaveURL('/');
  await expect(page.getByText('Today\'s Exclusive')).toBeVisible();
});

test('about page has call to action button', async ({ page }) => {
  await page.goto('/about');

  // Expect the "View Today's Design" button to be visible
  await expect(page.getByRole('link', { name: 'View Today\'s Design' })).toBeVisible();

  // Click the button
  await page.click('text=View Today\'s Design');
  
  // Expect to be on the home page
  await expect(page).toHaveURL('/');
  await expect(page.getByText('Today\'s Exclusive')).toBeVisible();
});