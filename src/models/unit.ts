export class Unit {
  public id: string
  public name: string
  public plural: string

  public constructor(id: string, name: string, plural: string) {
    this.id = id
    this.name = name
    this.plural = plural
  }
}

export async function getUnits(): Promise<Unit[]> {
  const response = await fetch('/api/unit')
  return (await response.json()) as Unit[]
}
