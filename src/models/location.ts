export class Location {
  public id: string
  public name: string
  public icon: string
  public is_freezer: boolean

  public constructor(id: string, name: string, icon: string, is_freezer: boolean) {
    this.id = id
    this.name = name
    this.icon = icon
    this.is_freezer = is_freezer
  }
}

export async function getLocations(): Promise<Location[]> {
  const response = await fetch('/api/location')
  return (await response.json()) as Location[]
}
