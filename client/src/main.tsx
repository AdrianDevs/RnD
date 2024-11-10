import { StrictMode } from 'react';
import { createRoot } from 'react-dom/client';
import { createBrowserRouter, RouterProvider } from 'react-router-dom';
import './index.css';
import Root from './routes/root.tsx';
import ErrorPage from './routes/error.tsx';
import About from './routes/about.tsx';
import { surveyDetailsAction, surveyDetailsLoader } from './routes/survey.tsx';
import API from './services/api.ts';
import Index from './routes/index.tsx';
import SurveyView from './routes/survey.tsx';
import EditSurvey, {
  surveyEditAction,
  surveyEditLoader,
} from './routes/survey-edit.tsx';
import { surveyDeleteAction } from './routes/survey-delete.tsx';

const router = createBrowserRouter([
  {
    path: '/',
    element: <Root />,
    errorElement: <ErrorPage />,
    loader: async () => await API.loadSurveys(),
    children: [
      {
        errorElement: <ErrorPage />,
        children: [
          { index: true, element: <Index /> },
          {
            path: 'surveys/:surveyId',
            element: <SurveyView />,
            loader: surveyDetailsLoader,
            action: surveyDetailsAction,
          },
          {
            path: 'surveys/:surveyId/edit',
            element: <EditSurvey />,
            loader: surveyEditLoader,
            action: surveyEditAction,
          },
          { path: 'surveys/:surveyId/destroy', action: surveyDeleteAction },
          {
            path: 'about',
            element: <About />,
          },
        ],
      },
    ],
  },
]);

createRoot(document.getElementById('root')!).render(
  <StrictMode>
    <RouterProvider router={router} />
  </StrictMode>
);
