import { useSubmit, useNavigate } from 'react-router-dom'
import { Button } from './ui/button'
import { Form } from './ui/form'
import { useForm } from 'react-hook-form'
import { Input } from './ui/input'

type Props = {
  onFilterChange: (filter: string) => void
}

const AppSidebarHeader = ({ onFilterChange }: Props) => {
  const navigate = useNavigate()
  const submit = useSubmit()

  const form = useForm()

  const onSubmit = () => {
    submit(
      { surveyId: 'new' },
      {
        method: 'post',
        action: `/surveys/new/edit`,
        encType: 'application/json',
      }
    )
  }

  return (
    <>
      <div className="flex h-full flex-col items-center justify-between px-4 pb-4 pt-2">
        <div
          className="cursor-pointer font-chapeau text-3xl font-medium text-white"
          onClick={() => {
            navigate('/')
          }}
        >
          Tracking Suits
        </div>
        <div className="flex flex-row justify-between gap-2 pt-3">
          <div>
            <Input
              className="border-purple_super_dark text-white focus:border-white focus-visible:ring-transparent"
              type="email"
              placeholder="Filter"
              onChange={(ev) => {
                onFilterChange(ev.target.value)
              }}
            />
          </div>
          <Form {...form}>
            {/* eslint-disable @typescript-eslint/no-misused-promises */}
            <form onSubmit={form.handleSubmit(onSubmit)} className="space-y-8">
              <Button
                className="hover:text-dark w-full bg-green_dark text-black hover:bg-green_medium"
                type="submit"
              >
                New
              </Button>
            </form>
          </Form>
        </div>
      </div>
    </>
  )
}

export default AppSidebarHeader
