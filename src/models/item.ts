import { createBlankLocation, Location } from '@/models/location.ts'
import { Unit } from '@/models/unit.ts'

export class Item {
  public id: string
  public name: string
  public location: Location
  public unit: Unit | undefined
  public unit_quantity: number | undefined

  public constructor(
    id: string,
    name: string,
    location: Location,
    unit: Unit | undefined,
    unit_quantity: number | undefined,
  ) {
    this.id = id
    this.name = name
    this.location = location
    this.unit = unit
    this.unit_quantity = unit_quantity
  }
}

export class ItemStore {
  public name: string
  public location_id: string
  public unit_id: string | undefined
  public unit_quantity: number | undefined

  constructor(item: Item) {
    this.name = item.name
    this.location_id = item.location.id
    this.unit_id = item.unit?.id
    this.unit_quantity = item.unit_quantity
  }
}

export async function getItems(): Promise<Item[]> {
  const response = await fetch('/api/item')
  return (await response.json()) as Item[]
}

export function createBlankItem(): Item {
  return new Item('', '', createBlankLocation(), undefined, undefined)
}

export async function storeItem(item: Item): Promise<Item | undefined> {
  let method = 'POST'
  let url = '/api/item'
  if (item.id !== '') {
    method = 'PUT'
    url = '/api/item/' + item.id
  }

  const response = await fetch(url, {
    method: method,
    headers: {
      'Content-type': 'application/json; charset=UTF-8',
    },
    body: JSON.stringify(new ItemStore(item)),
  })
  return (await response.json()) as Item
}
