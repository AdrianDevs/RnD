import {
  Sidebar,
  SidebarContent,
  SidebarGroup,
  SidebarGroupContent,
  SidebarGroupLabel,
  SidebarHeader,
  SidebarMenu,
  SidebarMenuButton,
  SidebarMenuItem,
} from '@/components/ui/sidebar';
import { Survey } from '@/services/api';
import { Inbox } from 'lucide-react';
import { NavLink, useLoaderData } from 'react-router-dom';
import AppSidebarHeader from './app-sidebar-header';
import { useEffect, useState } from 'react';

function AppSidebar() {
  const surveys = useLoaderData() as Survey[];
  const [filter, setFilter] = useState('');
  const [filteredSurveys, setFilteredSurveys] = useState(surveys);

  const onFilterChange = (text: string) => {
    setFilter(text);
  };

  useEffect(() => {
    console.log('surveys', surveys);
    const updatedSurveys = surveys.filter((survey) => {
      return survey.name.toLowerCase().includes(filter.toLowerCase());
    });
    setFilteredSurveys(updatedSurveys);
  }, [surveys, filter]);

  return (
    <Sidebar>
      <SidebarHeader>
        <SidebarMenu>
          <SidebarMenuItem>
            <AppSidebarHeader onFilterChange={onFilterChange} />
          </SidebarMenuItem>
        </SidebarMenu>
      </SidebarHeader>
      <SidebarContent>
        <SidebarGroup>
          <SidebarGroupLabel>Leads</SidebarGroupLabel>
          <SidebarGroupContent>
            <SidebarMenu>
              {filteredSurveys.map((survey) => (
                <SidebarMenuItem key={survey.id}>
                  <SidebarMenuButton asChild>
                    <NavLink
                      to={`surveys/${survey.id}`}
                      className={({ isActive, isPending }) =>
                        isActive ? 'active' : isPending ? 'pending' : ''
                      }
                    >
                      <Inbox />
                      <span>{survey.name}</span>
                    </NavLink>
                  </SidebarMenuButton>
                </SidebarMenuItem>
              ))}
            </SidebarMenu>
          </SidebarGroupContent>
        </SidebarGroup>
      </SidebarContent>
    </Sidebar>
  );
}

export default AppSidebar;
