import ApiMethods from './api_methods'

export type Brand = {
  id: number
  name: string
}

type answer_choice = {
  text: string
}

type question = {
  text: string
  question_type: {
    name: string
    description: string
  }
}

type questions_and_answer_choices = {
  question: question
  answer_choices: answer_choice[]
}

export type Survey = {
  id: number
  name: string
  description: string
  start_date: string
  end_date: string
  brand: { id: number; name: string }
  questions_and_answer_choices?: questions_and_answer_choices[]
}

const ENDPOINTS = {
  BRANDS: () => 'brands',
  SURVEYS: () => 'surveys/',
}

class API {
  static loadBrands = () => {
    const url = ENDPOINTS.BRANDS()
    return ApiMethods.get<Brand[]>(url)
  }

  static loadSurveys = () => {
    const url = ENDPOINTS.SURVEYS()
    return ApiMethods.get<Survey[]>(url)
  }

  static loadSurvey = (surveyId: number) => {
    const url = ENDPOINTS.SURVEYS() + surveyId
    return ApiMethods.get<Survey>(url)
  }

  static createSurvey = (
    survey: Omit<Survey, 'id' | 'brand'> & { brand_id: number }
  ) => {
    const url = ENDPOINTS.SURVEYS()
    return ApiMethods.post(url, survey)
  }

  static updateSurvey = (
    surveyId: number,
    survey: Omit<Survey, 'id' | 'brand'> & { brand_id: number }
  ) => {
    const url = ENDPOINTS.SURVEYS() + surveyId + '/'
    return ApiMethods.put(url, survey)
  }

  static deleteSurvey = (surveyId: number) => {
    const url = ENDPOINTS.SURVEYS() + surveyId + '/'
    return ApiMethods.delete(url)
  }
}

export default API
