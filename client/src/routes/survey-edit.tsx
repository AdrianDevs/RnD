/* eslint-disable react-refresh/only-export-components */
import {
  LoaderFunctionArgs,
  useLoaderData,
  useNavigate,
  useSubmit,
} from 'react-router-dom';
import { Calendar } from '@/components/ui/calendar';
import {
  Form,
  FormControl,
  FormDescription,
  FormField,
  FormItem,
  FormLabel,
  FormMessage,
} from '@/components/ui/form';
import { Input } from '@/components/ui/input';
import {
  Popover,
  PopoverContent,
  PopoverTrigger,
} from '@/components/ui/popover';
import {
  Select,
  SelectContent,
  SelectItem,
  SelectTrigger,
  SelectValue,
} from '@/components/ui/select';
import { cn } from '@/lib/utils';
import API, { Brand, Survey } from '@/services/api';
import { zodResolver } from '@hookform/resolvers/zod';
import { format } from 'date-fns';
import { CalendarIcon } from 'lucide-react';
import { useForm } from 'react-hook-form';
import { z } from 'zod';
import { Button } from '@/components/ui/button';

export async function surveyEditLoader({ params }: LoaderFunctionArgs) {
  const surveyId = params.surveyId;
  const survey =
    surveyId === 'new' ? null : await API.loadSurvey(Number(surveyId));
  const brands = await API.loadBrands();
  return { survey, brands };
}

export function surveyEditAction() {
  return null;
}

const formSchema = z.object({
  name: z.string().min(5, {
    message: 'The survey name must be at least 5 characters.',
  }),
  brand_id: z.string({ required_error: 'Please select a brand' }),
  description: z.string().min(5, { message: 'Please enter a description' }),
  start_date: z.date({
    required_error: 'Survey start date',
  }),
  end_date: z.date({
    required_error: 'Survey end date',
  }),
});

const EditSurvey = () => {
  const navigate = useNavigate();
  const submit = useSubmit();
  const { survey, brands } = useLoaderData() as {
    survey: Survey | null;
    brands: Brand[];
  };

  const today = new Date();
  const nextMonth = new Date(
    today.getFullYear(),
    today.getMonth() + 1,
    today.getDate()
  );

  const form = useForm<z.infer<typeof formSchema>>({
    resolver: zodResolver(formSchema),
    defaultValues: {
      name: survey?.name || '',
      description: survey?.description || '',
      brand_id: survey?.brand.id.toString() || '',
      start_date: today,
      end_date: nextMonth,
    },
  });

  async function onSubmit(values: z.infer<typeof formSchema>) {
    const params = {
      ...values,
      description: values.description || '',
      start_date: format(values.start_date, 'yyyy-MM-dd'),
      end_date: format(values.end_date, 'yyyy-MM-dd'),
      brand_id: parseInt(values.brand_id),
    };
    let newSurvey: Survey;
    if (!survey) {
      newSurvey = (await API.createSurvey(params)) as Survey;
    } else {
      newSurvey = (await API.updateSurvey(survey.id, params)) as Survey;
    }
    submit(
      { surveyId: `${newSurvey.id}` },
      {
        method: 'post',
        action: `/surveys/${newSurvey.id}`,
        encType: 'application/json',
      }
    );
  }

  return (
    <Form {...form}>
      {/* eslint-disable @typescript-eslint/no-misused-promises */}
      <form onSubmit={form.handleSubmit(onSubmit)} className="space-y-8">
        <FormField
          control={form.control}
          name="name"
          render={({ field }) => {
            return (
              <FormItem>
                <FormLabel>Name</FormLabel>
                <FormControl>
                  <Input placeholder="Enter a survey name" {...field} />
                </FormControl>
                <FormDescription>The name of the survey.</FormDescription>
                <FormMessage />
              </FormItem>
            );
          }}
        />
        <FormField
          control={form.control}
          name="brand_id"
          render={({ field }) => (
            <FormItem>
              <FormLabel>Brand</FormLabel>
              <Select onValueChange={field.onChange} defaultValue={field.value}>
                <FormControl>
                  <SelectTrigger>
                    <SelectValue placeholder="Select a brand" />
                  </SelectTrigger>
                </FormControl>
                <SelectContent>
                  {brands &&
                    brands.map((brand) => (
                      <SelectItem key={brand.id} value={brand.id.toString()}>
                        {brand.name}
                      </SelectItem>
                    ))}
                </SelectContent>
              </Select>
              <FormDescription>
                The brand that the survey is associated with.
              </FormDescription>
              <FormMessage />
            </FormItem>
          )}
        />
        <FormField
          control={form.control}
          name="description"
          render={({ field }) => {
            return (
              <FormItem>
                <FormLabel>Description</FormLabel>
                <FormControl>
                  <Input placeholder="Survey description" {...field} />
                </FormControl>
                <FormDescription>
                  The description of the survey.
                </FormDescription>
                <FormMessage />
              </FormItem>
            );
          }}
        />
        <FormField
          control={form.control}
          name="start_date"
          render={({ field }) => {
            return (
              <FormItem>
                <FormLabel>Start date</FormLabel>
                <Popover>
                  <PopoverTrigger asChild>
                    <FormControl>
                      <Button
                        variant={'outline'}
                        className={cn(
                          'w-[240px] pl-3 text-left font-normal',
                          !field.value && 'text-muted-foreground'
                        )}
                      >
                        {field.value ? (
                          format(field.value, 'PPP')
                        ) : (
                          <span>Pick a date</span>
                        )}
                        <CalendarIcon className="ml-auto h-4 w-4 opacity-50" />
                      </Button>
                    </FormControl>
                  </PopoverTrigger>
                  <PopoverContent className="w-auto p-0" align="start">
                    <Calendar
                      mode="single"
                      selected={field.value}
                      onSelect={field.onChange}
                      disabled={(date) =>
                        date > new Date() || date < new Date('1900-01-01')
                      }
                      initialFocus
                    />
                  </PopoverContent>
                </Popover>
                <FormDescription>
                  Your date of birth is used to calculate your age.
                </FormDescription>
                <FormMessage />
              </FormItem>
            );
          }}
        />
        <FormField
          control={form.control}
          name="end_date"
          render={({ field }) => {
            return (
              <FormItem>
                <FormLabel>End date</FormLabel>
                <Popover>
                  <PopoverTrigger asChild>
                    <FormControl>
                      <Button
                        variant={'outline'}
                        className={cn(
                          'w-[240px] pl-3 text-left font-normal',
                          !field.value && 'text-muted-foreground'
                        )}
                      >
                        {field.value ? (
                          format(field.value, 'PPP')
                        ) : (
                          <span>Pick a date</span>
                        )}
                        <CalendarIcon className="ml-auto h-4 w-4 opacity-50" />
                      </Button>
                    </FormControl>
                  </PopoverTrigger>
                  <PopoverContent className="w-auto p-0" align="start">
                    <Calendar
                      mode="single"
                      selected={field.value}
                      onSelect={field.onChange}
                      disabled={(date) =>
                        date > new Date() || date < new Date('1900-01-01')
                      }
                      initialFocus
                    />
                  </PopoverContent>
                </Popover>
                <FormDescription>
                  Your date of birth is used to calculate your age.
                </FormDescription>
                <FormMessage />
              </FormItem>
            );
          }}
        />
        <Button type="button" onClick={() => navigate(-1)}>
          Cancel
        </Button>
        <Button type="submit" disabled={!form.formState.isValid}>
          Submit
        </Button>
      </form>
    </Form>
  );
};

export default EditSurvey;