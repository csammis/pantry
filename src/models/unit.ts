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

class UnitStore {
  public name: string
  public plural: string

  public constructor(unit: Unit) {
    this.name = unit.name
    this.plural = unit.plural
  }
}

export async function getUnits(): Promise<Unit[]> {
  const response = await fetch('/api/unit')
  return (await response.json()) as Unit[]
}

export async function getUnit(id: string): Promise<Unit | undefined> {
  const response = await fetch('/api/unit/' + id)
  return (await response.json()) as Unit
}

export function createBlankUnit(): Unit {
  return new Unit('', '', '')
}

export async function storeUnit(unit: Unit): Promise<Unit | undefined> {
  let method = 'POST'
  let url = '/api/unit'
  if (unit.id !== '') {
    method = 'PUT'
    url = '/api/unit/' + unit.id
  }

  const response = await fetch(url, {
    method: method,
    headers: {
      'Content-type': 'application/json; charset=UTF-8',
    },
    body: JSON.stringify(new UnitStore(unit)),
  })
  return (await response.json()) as Unit
}

export async function deleteUnit(unit: Unit): Promise<boolean | undefined> {
  const response = await fetch('/api/unit/' + unit.id, {
    method: 'DELETE',
  })
  return response.ok
}
