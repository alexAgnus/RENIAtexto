import { Button, Spinner, Tab, Table, TableBody, TableCell, TableColumn, TableHeader, TableRow, Tabs, Textarea } from '@nextui-org/react'
import { NavbarComponent } from './NavbarComponent'
import { useState } from 'react'
import { Search } from 'iconoir-react'

interface PfsiCase {
  description: string
  id: number
  similarity: number
}

function App() {
  const [pfsiCases, setPfsiCases] = useState<PfsiCase[]>([]);
  const [description, setDescription] = useState<string>('');
  const [isLoading, setIsLoading] = useState<boolean>(false);

  const getPfsiCasesByDescription = () => {
    setIsLoading(true);
    setPfsiCases([]);
    fetch(`http://localhost:8000/api/get-similar-texts-with-universal-sentence-encoder?description=${description}`)
      .then(response => response.json())
      .then(data => {
        setIsLoading(false);
        setPfsiCases(data["data"]);
      })
  }

  return (
    <div className='w-full items-center flex flex-col gap-4'>
      <NavbarComponent />
      <p className='text-2xl font-bold'>Resultados de la busqueda</p>
      <div className="w-1/2 py-4 px-8 rounded-2xl flex justify-center items-center bg-gradient-to-tr from-blue-500 to-gray-500 text-white shadow-lg">
        <Textarea
          label="Search"
          radius="lg"
          value={description}
          isDisabled={isLoading}
          onChange={(e) => setDescription(e.target.value)}
          className='w-full'
          classNames={{
            label: "text-black/50 dark:text-white/90",
            input: [
              "bg-transparent",
              "text-black/90 dark:text-white/90",
              "placeholder:text-default-700/50 dark:placeholder:text-white/60",
            ],
            innerWrapper: "bg-transparent",
            inputWrapper: [
              "shadow-xl",
              "bg-default-200/50",
              "dark:bg-default/60",
              "backdrop-blur-xl",
              "backdrop-saturate-200",
              "hover:bg-default-200/70",
              "dark:hover:bg-default/70",
              "group-data-[focused=true]:bg-default-200/50",
              "dark:group-data-[focused=true]:bg-default/60",
              "!cursor-text",
            ],
          }}
          placeholder="Type to search..."
        />
        <Button
          isDisabled={isLoading}
          className='ml-4'
          onClick={() => getPfsiCasesByDescription()}
          endContent={<Search className='w-48' />}
        >
          Search
        </Button>
      </div>
      <Tabs aria-label="Options" className='w-1/2'>
        <Tab key="photos" title="Missing persons" className='w-full'>
          <div className='px-48 w-full'>
            <Table className='w-full' classNames={{
              table: "min-h-[400px]",
            }}>
              <TableHeader>
                <TableColumn>Id</TableColumn>
                <TableColumn>Similarity</TableColumn>
                <TableColumn>Description</TableColumn>
              </TableHeader>
              <TableBody isLoading={isLoading} loadingContent={<Spinner label="Loading..." />}>
                {
                  pfsiCases.map((pfsiCase, index) => (
                    <TableRow key={index}>
                      <TableCell> {pfsiCase.id} </TableCell>
                      <TableCell> {pfsiCase.similarity} </TableCell>
                      <TableCell> {pfsiCase.description} </TableCell>
                    </TableRow>
                  ))
                }
              </TableBody>
            </Table>
          </div>
        </Tab>
        <Tab key="music" title="By location">
          <div>
            <iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3988.880508821748!2d-77.0420656857368!3d-12.046607991474403!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0xcee3f6b0b0b0b0b0%3A0x9e1b0b0b0b0b0b0!2sPlaza%20de%20Armas%20de%20Lima!5e0!3m2!1ses-419!2spe!4v1629787306784!5m2!1ses-419!2spe"
              width="1000"
              className='border border-gray-200 rounded-xl shadow-md'
              height="600"
              loading="lazy">
            </iframe>
          </div>
        </Tab>
      </Tabs>
    </div>
  )
}

export default App
