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

class LocationStore {
  public name: string
  public icon: string
  public is_freezer: boolean

  public constructor(location: Location) {
    this.name = location.name
    this.icon = location.icon
    this.is_freezer = location.is_freezer
  }
}

let locationCache: Location[] = []

export async function getLocations(): Promise<Location[]> {
  if (locationCache.length == 0) {
    const response = await fetch('/api/location')
    await response.json().then(function (resp: Location[]) {
      locationCache = resp
      return resp
    })
  }
  return locationCache
}

export async function getLocation(id: string): Promise<Location | undefined> {
  const response = await fetch('/api/location/' + id)
  return (await response.json()) as Location
}

export function createBlankLocation(): Location {
  return new Location('', '', '', false)
}

export async function storeLocation(location: Location): Promise<Location | undefined> {
  let method = 'POST'
  let url = '/api/location'
  if (location.id !== '') {
    method = 'PUT'
    url = '/api/location/' + location.id
  }

  const response = await fetch(url, {
    method: method,
    headers: {
      'Content-type': 'application/json; charset=UTF-8',
    },
    body: JSON.stringify(new LocationStore(location)),
  })
  return (await response.json()) as Location
}

export async function deleteLocation(location: Location): Promise<boolean | undefined> {
  const response = await fetch('/api/location/' + location.id, {
    method: 'DELETE',
  })
  return response.ok
}
