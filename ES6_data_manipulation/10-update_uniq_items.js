export default function updateUniqueItems(groceries) {
  if (!(groceries instanceof Map)) {
    throw new Error('Cannot process');
  }

  for (const [key, quanity] of groceries) {
    if (quanity === 1) {
      groceries.set(key, 100);
    }
  }

  return groceries;
}
