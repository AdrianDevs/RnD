import { StrictMode } from 'react';
import { createRoot } from 'react-dom/client';
import { createBrowserRouter, RouterProvider } from 'react-router-dom';
import './index.css';
import Root from './routes/root.tsx';
import ErrorPage from './routes/error.tsx';
import About from './routes/about.tsx';
import Survey from './routes/survey.tsx';
import API from './services/api.ts';
import Index from './routes/index.tsx';
import NewSurvey from './routes/survey-new.tsx';

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
            path: 'surveys/new',
            element: <NewSurvey />,
            loader: async () => await API.loadBrands(),
          },
          {
            path: 'surveys/:surveyId',
            element: <Survey />,
          },
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
