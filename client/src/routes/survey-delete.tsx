import API from '@/services/api'
import { ActionFunctionArgs, redirect } from 'react-router-dom'

export async function surveyDeleteAction({ params }: ActionFunctionArgs) {
    await API.deleteSurvey(Number(params.surveyId))
    return redirect('/')
}
