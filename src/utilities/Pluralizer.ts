export function makeSingularOrPlural(
  quantity: number,
  singular: string,
  plural: string | undefined,
): string {
  // Extremely locale un-aware
  if (quantity == 1 || plural === undefined) {
    return singular
  } else {
    return plural
  }
}
