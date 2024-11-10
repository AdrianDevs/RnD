/* eslint-disable react-refresh/only-export-components */
import API from '@/services/api';
import {
  LoaderFunctionArgs,
  useLoaderData,
  useNavigate,
  useSubmit,
} from 'react-router-dom';
import { Survey } from '@/services/api';
import { Button } from '@/components/ui/button';

export async function surveyDetailsLoader({ params }: LoaderFunctionArgs) {
  const surveyId = Number(params.surveyId);
  const survey = await API.loadSurvey(surveyId);
  return survey;
}

export function surveyDetailsAction() {
  return null;
}

const SurveyView = () => {
  const navigate = useNavigate();
  const submit = useSubmit();
  const survey = useLoaderData() as Survey;

  const onCancelClick = () => {
    return navigate('/');
  };

  const onEditClick = () => {
    submit(
      { surveyId: `${survey.id}` },
      {
        method: 'post',
        action: `/surveys/${survey.id}/edit`,
        encType: 'application/json',
      }
    );
  };

  const onDeleteClick = () => {
    submit(
      { surveyId: `${survey.id}` },
      {
        method: 'post',
        action: 'destroy',
      }
    );
  };

  return (
    <div>
      <h1>{survey.name}</h1>
      <Button type="button" onClick={onCancelClick}>
        Back
      </Button>
      <Button type="button" onClick={onEditClick}>
        Edit
      </Button>
      <Button type="button" onClick={onDeleteClick}>
        Delete
      </Button>
    </div>
  );
};

export default SurveyView;
