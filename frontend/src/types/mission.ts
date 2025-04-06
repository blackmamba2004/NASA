export interface SolActivity {
    sol: number;
    earth_date: string;
    total_photos: number;
    cameras: string[];
}
  
export interface Paginator {
    page: number;
    total: number;
    has_prev: boolean;
    has_next: boolean;
}

export interface MissionDataResponse {
    paginator: Paginator;
    data: {
        photo_manifest: {
        name: string;
        landing_date: string;
        launch_date: string;
        status: string;
        max_sol: number;
        max_date: string;
        total_photos: number;
        sol_activities: SolActivity[];
        };
    };
}

export enum RoverNameEnum {
    CURIOSITY = 'Curiosity',
    OPPORTUNITY = 'Opportunity',
    PERSEVERANCE = 'Perseverance',
    SPIRIT = 'Spirit',
}
  
export enum RoverCameraEnum {
    FHAZ = 'fhaz',
    RHAZ = 'rhaz',
    MAST = 'mast',
    CHEMCAM = 'chemcam',
    MAHLI = 'mahli',
    MARDI = 'mardi',
    NAVCAM = 'navcam',
    PANCAM = 'pancam',
    MINITES = 'minites',
}
  