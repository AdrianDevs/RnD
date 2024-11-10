import { useNavigate } from 'react-router-dom';
import { Button } from './ui/button';

const AppSidebarHeader = () => {
  const navigate = useNavigate();

  const onClick = () => {
    navigate('/surveys/new');
  };

  return (
    <div className="flex items-center justify-between h-16 px-4 border-b border-gray-200">
      <div className="flex items-center">
        <div className="text-lg font-semibold text-gray-800">
          Tracking Suits
        </div>
        <Button
          className="ml-2 p-1 text-gray-500 rounded-md hover:bg-gray-100"
          onClick={onClick}
        >
          New
        </Button>
      </div>
    </div>
  );
};

export default AppSidebarHeader;
