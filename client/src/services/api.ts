import ApiMethods from './api_methods';

export type Brand = {
  id: number;
  name: string;
};

export type Survey = {
  id: number;
  name: string;
  description: string;
  start_date: string;
  end_date: string;
  brand_name: string;
};

const ENDPOINTS = {
  BRANDS: () => 'brands',
  SURVEY: () => 'surveys/',
};

class API {
  static loadBrands = () => {
    const url = ENDPOINTS.BRANDS();
    return ApiMethods.get<Brand[]>(url);
  };
  static loadSurveys = () => {
    const url = ENDPOINTS.SURVEY();
    return ApiMethods.get<Survey[]>(url);
  };
  static createSurvey = (
    survey: Omit<Survey, 'id' | 'brand_name'> & { brand_id: number }
  ) => {
    const url = ENDPOINTS.SURVEY();
    return ApiMethods.post(url, survey);
  };
}

export default API;
