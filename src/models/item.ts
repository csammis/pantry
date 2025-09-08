import { Location } from '@/models/location.ts'
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
  public location: Location
  public unit: Unit | undefined
  public unit_quantity: number | undefined

  public constructor(item: Item) {
    this.name = item.name
    this.location = item.location
    this.unit = item.unit
    this.unit_quantity = item.unit_quantity
  }
}

export async function getItems(): Promise<Item[]> {
  const response = await fetch('/api/item')
  return (await response.json()) as Item[]
}
