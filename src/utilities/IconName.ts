//! Transform a kebab-case Material Design Icon name to the mdiCamelCase that mdi/js wants
export function transformKebabCaseToMdiJs(name: string): string {
  const words = name.split('-').map((str) => str[0].toUpperCase() + str.slice(1))
  return 'mdi' + words.join('')
}
