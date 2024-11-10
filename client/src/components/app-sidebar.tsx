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
} from '@/components/ui/sidebar'
import { Survey } from '@/services/api'
import { Inbox, UserPen } from 'lucide-react'
import { NavLink, useLoaderData } from 'react-router-dom'
import AppSidebarHeader from './app-sidebar-header'
import { useEffect, useState } from 'react'
import { filterSurveys } from '@/lib/utils'

function AppSidebar() {
  const surveys = useLoaderData() as Survey[]
  const [filter, setFilter] = useState('')
  const [filteredSurveys, setFilteredSurveys] = useState(surveys)

  const onFilterChange = (text: string) => {
    setFilter(text)
  }

  useEffect(() => {
    const updatedSurveys = filterSurveys(surveys, filter)
    setFilteredSurveys(updatedSurveys)
  }, [surveys, filter])

  return (
    <Sidebar>
      <SidebarHeader className="bg-purple_dark p-0">
        <SidebarMenu>
          <SidebarMenuItem>
            <AppSidebarHeader onFilterChange={onFilterChange} />
          </SidebarMenuItem>
        </SidebarMenu>
      </SidebarHeader>
      <SidebarContent className="bg-gradient-to-b from-purple_dark to-merino">
        <SidebarGroup>
          <SidebarGroupLabel className="my-2 text-2xl text-text_dark">
            Surveys
          </SidebarGroupLabel>
          <SidebarGroupContent>
            <SidebarMenu>
              {filteredSurveys.map((survey) => {
                return (
                  <SidebarMenuItem key={survey.id}>
                    <SidebarMenuButton asChild>
                      <NavLink to={`surveys/${survey.id}`}>
                        <Inbox color="black" />
                        <span className="font-semibold text-text_dark">
                          {survey.name}
                        </span>
                      </NavLink>
                    </SidebarMenuButton>
                  </SidebarMenuItem>
                )
              })}
            </SidebarMenu>
            <SidebarMenu>
              <SidebarMenuItem className="mt-8 rounded-md bg-merino">
                <SidebarMenuButton asChild>
                  <NavLink to="about">
                    <UserPen color="black" />
                    <span className="font-semibold text-text_dark">About</span>
                  </NavLink>
                </SidebarMenuButton>
              </SidebarMenuItem>
            </SidebarMenu>
          </SidebarGroupContent>
        </SidebarGroup>
      </SidebarContent>
    </Sidebar>
  )
}

export default AppSidebar
