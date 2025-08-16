// tests/archive.spec.js
import { test, expect } from '@playwright/test';

test('archive page displays shirt designs', async ({ page }) => {
  await page.goto('/archive');

  // Expect the page title to contain "AI Generated Clothing"
  await expect(page).toHaveTitle(/AI Generated Clothing/);

  // Expect the archive heading to be visible
  await expect(page.getByText('Design Archive')).toBeVisible();

  // Expect to see multiple shirt designs
  const shirtImages = await page.$$('img');
  expect(shirtImages.length).toBeGreaterThan(0);

  // Expect to see shirt topics
  await expect(page.getByText('Machine Learning')).toBeVisible();
  await expect(page.getByText('Neural Networks')).toBeVisible();
});

test('archive page navigation works', async ({ page }) => {
  await page.goto('/archive');

  // Click on the Home link
  await page.click('text=Home');
  
  // Expect to be on the home page
  await expect(page).toHaveURL('/');
  await expect(page.getByText('Today\'s Exclusive')).toBeVisible();
});