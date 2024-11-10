import { useSubmit } from 'react-router-dom';
import { Button } from './ui/button';
import { Form } from './ui/form';
import { useForm } from 'react-hook-form';
import { Input } from './ui/input';

type Props = {
  onFilterChange: (filter: string) => void;
};

const AppSidebarHeader = ({ onFilterChange }: Props) => {
  const submit = useSubmit();

  const form = useForm();

  const onSubmit = () => {
    submit(
      { surveyId: 'new' },
      {
        method: 'post',
        action: `/surveys/new/edit`,
        encType: 'application/json',
      }
    );
  };

  return (
    <div className="flex items-center justify-between h-16 px-4 border-b border-gray-200">
      <div className="flex items-center">
        <div className="text-lg font-semibold text-gray-800">
          Tracking Suits
        </div>
        <Form {...form}>
          {/* eslint-disable @typescript-eslint/no-misused-promises */}
          <form onSubmit={form.handleSubmit(onSubmit)} className="space-y-8">
            <Button type="submit">New</Button>
          </form>
        </Form>
        <div>
          <Input
            type="email"
            placeholder="Filter"
            onChange={(ev) => {
              onFilterChange(ev.target.value);
            }}
          />
        </div>
      </div>
    </div>
  );
};

export default AppSidebarHeader;
