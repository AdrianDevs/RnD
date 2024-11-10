/* eslint-disable react-refresh/only-export-components */
import API from '@/services/api'
import {
  LoaderFunctionArgs,
  useLoaderData,
  useNavigate,
  useSubmit,
} from 'react-router-dom'
import { Survey } from '@/services/api'
import { Button } from '@/components/ui/button'

export async function surveyDetailsLoader({ params }: LoaderFunctionArgs) {
  const surveyId = Number(params.surveyId)
  const survey = await API.loadSurvey(surveyId)
  return survey
}

export function surveyDetailsAction() {
  return null
}

const SurveyView = () => {
  const navigate = useNavigate()
  const submit = useSubmit()
  const survey = useLoaderData() as Survey

  const onCancelClick = () => {
    return navigate('/')
  }

  const onEditClick = () => {
    submit(
      { surveyId: `${survey.id}` },
      {
        method: 'post',
        action: `/surveys/${survey.id}/edit`,
        encType: 'application/json',
      }
    )
  }

  const onDeleteClick = () => {
    submit(
      { surveyId: `${survey.id}` },
      {
        method: 'post',
        action: 'destroy',
      }
    )
  }

  return (
    <div className="flex flex-row justify-center">
      <div className="flex flex-col justify-start rounded-2xl bg-green_medium p-16">
        <h1 className="font-chapeau text-5xl font-light text-black">
          {survey.name}
        </h1>
        <div className="mt-2 flex flex-row items-center justify-between px-8 py-4">
          <Button
            className="m-2 w-full bg-purple_super_dark hover:bg-purple_medium hover:text-text_dark"
            type="button"
            onClick={onCancelClick}
          >
            Back
          </Button>
          <Button
            className="m-2 w-full bg-purple_super_dark hover:bg-purple_medium hover:text-text_dark"
            type="button"
            onClick={onEditClick}
          >
            Edit
          </Button>
          <Button
            className="m-2 w-full bg-pink_dark hover:bg-pink_medium hover:text-text_dark"
            type="button"
            onClick={onDeleteClick}
          >
            Delete
          </Button>
        </div>
        <h2 className="pb-4 font-chapeau text-3xl">{survey.brand.name}</h2>
        <div>
          <p>
            from {survey.start_date} to {survey.end_date}
          </p>
        </div>
        <div>
          <h3 className="py-4 text-2xl font-semibold">Description</h3>
          <p>{survey.description}</p>
        </div>
        <h2 className="py-4 text-2xl font-semibold">Questions</h2>
        <div>
          {survey.questions_and_answer_choices?.map((qa) => (
            // <div>{qa.question ? 'hello' : 'bye'}</div>
            <div key={qa.question.text}>
              <h3 className="py-1">
                {qa.question.text.replace(/{brand}/g, survey.brand.name)}
              </h3>
              <ul className="list-disc ps-4">
                {qa.answer_choices.map((ac) => (
                  <li key={ac.text} className="pt-1">
                    {ac.text}
                  </li>
                ))}
              </ul>
            </div>
          ))}
        </div>
      </div>
    </div>
  )
}

export default SurveyView
