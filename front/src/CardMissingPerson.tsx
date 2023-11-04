import { Card, CardHeader } from '@nextui-org/react'

export const CardMissingPerson = ({ description }: { description: string }) => {
  return (
    <Card className="py-4 w-max">
      <CardHeader className="pb-0 pt-2 px-4 flex-col items-start">
        <p className="text-tiny uppercase font-bold">{ description }</p>
        <small className="text-default-500">20 years</small>
        <p className="text-default-500 font-bold text-sm">Frontend Radio</p>
      </CardHeader>
      {/*   <CardBody className="overflow-visible py-2">
          <Image
            alt="Card background"
            className="object-cover rounded-xl"
            src="https://nextui.org/images/hero-card-complete.jpeg"
            width={270}
            isZoomed
          />
        </CardBody> */}
    </Card>
  )
}