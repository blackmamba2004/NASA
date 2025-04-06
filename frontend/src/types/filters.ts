import { RoverCameraEnum, RoverNameEnum } from './mission';

export interface Filters {
  rover_name: RoverNameEnum | string;
  sol_from: number | null;
  sol_to: number | null;
  earth_date_from: string | null;
  earth_date_to: string | null;
  min_total_photo: number | null;
  max_total_photo: number | null;
  cameras: RoverCameraEnum[];
  page: number;
  size: number;
}
